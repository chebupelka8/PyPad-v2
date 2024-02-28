from scr.scripts import FileLoader, FileChecker
from scr.config import IconPaths
from .welcome_screen import WelcomeScreen

from PySide6.QtWidgets import QTabWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

from typing import Any, Optional, Union


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

    def get_all_info_tabs(
            self,
            only_files: bool = False,
            key: Optional[str] = None,
            should_dict: bool = False
    ) -> Union[dict, list]:
        """
        for files:
            title,
            widget,
            icon,
            path

        for other:
            title,
            widget,
            icon
        """
        result = {}

        for i, widget in enumerate(self.get_all_tabs()):
            if hasattr(widget, "get_full_path"):
                result[str(i)] = {
                    "title": self.tabText(i),
                    "widget": self.widget(i),
                    "icon": self.tabIcon(i),
                    "index": i,
                    "path": widget.get_full_path()
                }

            elif not hasattr(widget, "get_full_path") and not only_files:
                result[str(i)] = {
                    "title": self.tabText(i),
                    "widget": self.widget(i),
                    "icon": self.tabIcon(i),
                    "index": i
                }

        match key:
            case key if key is None:
                return result if should_dict else [list(result[i].values()) for i in result.keys()]

            case key if isinstance(key, str):
                return [result[item][key] for item in result.keys()]

            # case keys if isinstance(key, list):
            #     res = []
            #
            #     for j in result.keys():
            #         for subkey in result[j].keys():
            #             if exclusion_keys is not None:
            #                 if subkey in keys and subkey not in exclusion_keys:
            #                     res.append(result[j][subkey])
            #
            #             else:
            #                 if subkey in keys:
            #                     res.append(result[j][subkey])

    def check_tab_paths_exist(self) -> None:
        # return self.get_all_info_tabs(True, key="path")

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
        for widget in self.get_all_info_tabs(True, key="widget"):
            if widget.get_full_path() == __path:
                return widget

    def get_all_tabs(self) -> list[Any]:
        return [self.widget(i) for i in range(self.count())]

    def get_all_paths(self):
        return self.get_all_info_tabs(True, key="path")

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
