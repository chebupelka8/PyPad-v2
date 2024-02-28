from scr.scripts import FileLoader, FileChecker
from scr.config import IconPaths
from .welcome_screen import WelcomeScreen

from PySide6.QtWidgets import QTabWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

from typing import Any


class TabEditor(QTabWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/tab_editor.css"))
        self.setObjectName("tab-editor")
        self.setMinimumSize(1040, 480)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.setTabsClosable(True)
        self.setMovable(True)
        self.setMouseTracking(True)
        self.setIconSize(QSize(16, 16))
        self.tabCloseRequested.connect(self.removeTab)

    def check_tab_paths_exist(self):
        for i, widget in enumerate(self.get_all_tabs()):
            if hasattr(widget, "get_full_path"):
                if not FileChecker.check_exist(widget.get_full_path()):
                    self.removeTab(i)

    def update_all_tabs_font(self) -> None:
        for widget in self.get_all_tabs():
            if hasattr(widget, "update_font"):
                widget.update_font()

    def update_all_tabs_settings(self) -> None:
        for widget in self.get_all_tabs():
            if hasattr(widget, "update_settings"):
                widget.update_settings()

    def find_by_path(self, __path: str):
        for widget in self.get_all_tabs():
            if hasattr(widget, "get_full_path"):
                if widget.get_full_path() == __path:
                    return widget

    def get_all_tabs(self) -> list[Any]:
        return [self.widget(i) for i in range(self.count())]

    def get_all_paths(self):
        res = []

        for widget in self.get_all_tabs():
            if hasattr(widget, "get_full_path"):
                res.append(widget.get_full_path())

        return res

    def get_current_path(self) -> str:
        if hasattr(self.currentWidget(), "get_full_path"):
            return self.currentWidget().get_full_path()
        else:
            return ""  # it's need to remove exception

    def removeTab(self, __index: int):
        super().removeTab(__index)

        if self.count() == 0:
            self.addTab(WelcomeScreen(), "Welcome!", IconPaths.SystemIcons.WELCOME)

    def addTab(self, widget: Any, arg__2, icon=None):
        if hasattr(widget, "get_full_path"):
            path = widget.get_full_path()

            if path not in self.get_all_paths():
                super().addTab(widget, arg__2)
            else:
                self.setCurrentWidget(self.find_by_path(path))
        else:
            super().addTab(widget, arg__2)

        if icon is not None:
            self.setTabIcon(self.indexOf(widget), QIcon(icon))
