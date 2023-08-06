from typing import List, Tuple, Iterable, Set, Optional, Dict, cast
import pkg_resources
from dataclasses import dataclass

import urwid
from urwid import signals

from ovshell.protocol import ScreenManager, Activity, OpenVarioShell
from ovshell.protocol import Extension, ExtensionFactory
from ovshell import widget
from ovshell import protocol
from ovshell import settings
from ovshell import ovos


@dataclass
class ActivityContext:
    activity: protocol.Activity
    widget: urwid.Widget
    palette: Dict[str, Tuple]


class TopBar(urwid.WidgetWrap):
    def __init__(self) -> None:
        w = urwid.Text("Openvario")
        super().__init__(urwid.AttrMap(w, "topbar"))


class FooterBar(urwid.WidgetWrap):
    def __init__(self) -> None:
        super().__init__(urwid.AttrMap(urwid.Divider(), "bg"))


class ScreenManagerImpl(ScreenManager):
    def __init__(self, mainloop: urwid.MainLoop) -> None:
        self._mainloop = mainloop
        self._main_view = urwid.WidgetPlaceholder(urwid.SolidFill(" "))
        self.layout = self._create_layout()
        self._act_stack: List[ActivityContext] = []

        self._mainloop.widget = self.layout

    def _create_layout(self) -> urwid.Widget:
        btxt = urwid.BigText("Openvario", urwid.font.Thin6x6Font())
        splash = urwid.Filler(urwid.Padding(btxt, "center", "clip"), "middle")
        self._main_view.original_widget = splash
        return urwid.Frame(self._main_view, header=TopBar(), footer=FooterBar())

    def push_activity(self, activity: Activity, palette: List[Tuple] = None) -> None:
        w = activity.create()
        signals = widget.KeySignals(urwid.AttrMap(w, widget.NORMAL_ATTR_MAP))
        urwid.connect_signal(
            signals, "cancel", self._cancel_activity, user_args=[activity]
        )
        if palette is not None:
            self._mainloop.screen.register_palette(palette)
            self._mainloop.screen.clear()
        self._main_view.original_widget = signals
        activity.activate()
        self._act_stack.append(
            ActivityContext(activity, signals, palette=self._get_palette())
        )

    def push_modal(self, activity: Activity, options: protocol.ModalOptions) -> None:
        bg = self._main_view.original_widget
        modal_w = activity.create()
        modal_w = urwid.AttrMap(modal_w, widget.LIGHT_ATTR_MAP)
        signals = widget.KeySignals(modal_w)
        urwid.connect_signal(
            signals, "cancel", self._cancel_activity, user_args=[activity]
        )
        modal = urwid.Overlay(
            signals,
            bg,
            align=options.align,
            width=options.width,
            valign=options.valign,
            height=options.height,
            min_width=options.min_width,
            min_height=options.min_height,
            left=options.left,
            right=options.right,
            top=options.top,
            bottom=options.bottom,
        )
        self._main_view.original_widget = modal
        activity.activate()
        self._act_stack.append(
            ActivityContext(activity, modal, palette=self._get_palette())
        )

    def pop_activity(self) -> None:
        curactctx = self._act_stack.pop()
        curactctx.activity.destroy()

        prevactctx = self._act_stack[-1]
        self._main_view.original_widget = prevactctx.widget
        prevactctx.activity.activate()
        self._reset_palette(prevactctx.palette)

    def _cancel_activity(self, activity: Activity, w: urwid.Widget) -> None:
        self.pop_activity()

    def _get_palette(self) -> Dict[str, Tuple]:
        return self._mainloop.screen._palette.copy()

    def _reset_palette(self, palette: Dict[str, Tuple]):
        # Reset the palette for activity. We use a bit of urwid implementation
        # details here, because of lack of public way to do this.
        self._mainloop.screen._palette = palette.copy()
        for name, entry in palette.items():
            (basic, mono, high_88, high_true) = entry
            signals.emit_signal(
                self._mainloop.screen,
                urwid.UPDATE_PALETTE_ENTRY,
                name,
                basic,
                mono,
                high_88,
                high_true,
            )
        self._mainloop.screen.clear()


class ExtensionManagerImpl(protocol.ExtensionManager):
    _extensions: List[Extension]

    def __init__(self):
        self._extensions = []

    def load_all(self, shell: OpenVarioShell) -> None:
        for entry_point in pkg_resources.iter_entry_points("ovshell.extensions"):
            extfactory = cast(ExtensionFactory, entry_point.load())
            ext = extfactory(entry_point.name, shell)
            self._extensions.append(ext)
            print(f"Loaded extension: {ext.title}")

    def list_extensions(self) -> Iterable[Extension]:
        return self._extensions


class AppManagerImpl(protocol.AppManager):
    def __init__(self, shell: OpenVarioShell) -> None:
        self.shell = shell

    def list(self) -> Iterable[protocol.AppInfo]:
        appinfos = []
        allpinned = self._get_pinned()
        for ext in self.shell.extensions.list_extensions():
            for app in ext.list_apps():
                appid = f"{ext.id}.{app.name}"
                appinfo = protocol.AppInfo(
                    id=appid, app=app, extension=ext, pinned=appid in allpinned,
                )
                appinfos.append(appinfo)

        appinfos = sorted(appinfos, key=lambda v: (-v.app.priority, v.extension.id))
        return appinfos

    def pin(self, app: protocol.AppInfo, persist: bool = False) -> None:
        pinned = self._get_pinned()
        if app.id in pinned:
            return
        pinned.add(app.id)
        self._set_pinned(pinned, persist)

    def unpin(self, app: protocol.AppInfo, persist: bool = False) -> None:
        pinned = self._get_pinned()
        if app.id not in pinned:
            return
        pinned.remove(app.id)
        self._set_pinned(pinned, persist)

    def install_new_apps(self) -> List[protocol.AppInfo]:
        installed = self.shell.settings.get("ovshell.installed_apps", list) or []
        newapps = []
        for appinfo in self.list():
            if appinfo.id in installed:
                continue

            print(f"Installing new app {appinfo.id}")
            appinfo.app.install(appinfo)
            installed.append(appinfo.id)
            newapps.append(appinfo)

        if newapps:
            self.shell.settings.set("ovshell.installed_apps", sorted(installed), True)

        return newapps

    def _get_pinned(self) -> Set[str]:
        return set(self.shell.settings.get("ovshell.pinned_apps", list) or [])

    def _set_pinned(self, pinned: Set[str], persist: bool = False):
        self.shell.settings.set("ovshell.pinned_apps", sorted(pinned) or [])


class OpenvarioShellImpl(OpenVarioShell):
    def __init__(
        self, screen: ScreenManager, config: str, rootfs: Optional[str]
    ) -> None:
        self.screen = screen
        if rootfs is None:
            self.os = ovos.OpenVarioOSImpl()
        else:
            print(f"Simulating Openvario on {rootfs}")
            self.os = ovos.OpenVarioOSSimulator(rootfs)
        self.settings = settings.StoredSettingsImpl.load(config)
        self.devices = None
        self.processes = None
        self.extensions = ExtensionManagerImpl()
        self.apps = AppManagerImpl(self)

    def quit(self) -> None:
        raise urwid.ExitMainLoop()
