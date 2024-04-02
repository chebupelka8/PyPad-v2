from scr.scripts.tools.file import FileLoader, FileChecker
from scr.configs.pics import IconPaths
from .welcome_screen import WelcomeScreen

from scr.scripts.font import WorkbenchFontManager

from PySide6.QtWidgets import QTabWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

from typing import Any, Optional, Union

from dataclasses import dataclass


@dataclass
class Tab:
    """
    Represents a tab in the Tab Editor.

    Attributes:
    - title: str - The title of the tab.
    - widget: Any - The content widget of the tab.
    - icon: Union[QIcon, str, None] - The icon associated with the tab.
    - path: Optional[str] - The file path associated with the tab.
    - index: Optional[int] - The index of the tab.

    Methods:
    - is_file(): bool - Checks if the tab is associated with a file.
    - is_readable(): bool - Checks if the file associated with the tab is readable.
    - __post_init__(): None - Initializes the tab with an icon if it's a string.
    - __repr__(): str - Returns a string representation of the tab.
    """

    # todo: add 'pinned tabs'
    # todo: add var 'is_pinned' and it must be at the beginning of the tab editor

    title: str
    widget: Any
    icon: Union[QIcon, str, None] = None
    path: Optional[str] = None
    index: Optional[int] = None

    def is_file(self) -> bool:
        return self.path is not None

    def is_readable(self) -> bool:
        return FileChecker.is_readable(self.path)

    def __post_init__(self) -> None:
        if isinstance(self.icon, str):
            self.icon = QIcon(self.icon)

    def __repr__(self) -> str:
        return f"Tab(title={self.title}, widget={self.widget}, icon={self.icon}, path={self.path}, index={self.index})"


class TabEditor(QTabWidget):
    """
    Custom Tab Widget for managing tabs.

    Methods:
    - __init__(): None - Initializes the Tab Editor.
    - update_font(): None - Updates the font settings for the Tab Editor.
    - get_tabs(): list[Tab] - Returns a list of all tabs.
    - get_current_tab(): Optional[Tab] - Returns the current active tab.
    - __get_json_info(): dict - Returns tab information in JSON format.
    - get_info_tabs(key: str, only_files: bool = False): list - Retrieves specific information from tabs.
    - check_tab_paths_exist(): None - Checks if tab paths exist and removes invalid tabs.
    - update_all_tabs_font(): None - Updates font settings for all tabs.
    - update_all_tabs_settings(): None - Updates settings for all tabs.
    - find_by_path(__path: str): Any - Finds a widget by its associated path.
    - get_all_widgets(): list[Any] - Returns all widgets in the Tab Editor.
    - get_all_paths(): list - Returns paths of all file tabs.
    - get_current_path(): str - Returns the path of the current active tab.
    - __update_indexes(): None - Updates tab indexes.
    - removeTab(__index: int): None - Removes a tab by index.
    - add_tab(tab: Tab): None - Adds a new tab to the Tab Editor.
    """

    def __init__(self) -> None:
        super().__init__()

        self.__tabs: list[Tab] = []

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/tab_editor.css"))
        self.setObjectName("tab-editor")
        self.setMinimumSize(1040, 480)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.__main_font = WorkbenchFontManager.get_current_font_as_font()
        self.update_font()

        self.setTabsClosable(True)
        self.setMovable(True)
        self.setMouseTracking(True)
        self.tabCloseRequested.connect(self.removeTab)
        self.currentChanged.connect(self.__update_indexes)

    def update_font(self) -> None:
        self.__main_font = WorkbenchFontManager.get_current_font_as_font()
        self.setIconSize(QSize(self.__main_font.pointSize() * 1.3, self.__main_font.pointSize() * 1.3))
        self.__main_font.setPointSize(self.__main_font.pointSize())
        self.setFont(self.__main_font)

    def get_tabs(self) -> list[Tab]:
        return self.__tabs

    def get_current_tab(self) -> Optional[Tab]:
        try:
            return self.__tabs[self.currentIndex()]

        except IndexError:
            return None

    def __get_json_info(self) -> dict:
        res = {}

        for i, tab in enumerate(self.__tabs):
            res[str(i)] = {
                "title": tab.title,
                "widget": tab.widget,
                "icon": tab.icon,
                "path": tab.path,
                "index": tab.index
            }

        return res

    def get_info_tabs(self, key: str, only_files: bool = False) -> list:
        res = []
        jsn = self.__get_json_info()

        for tab in jsn.keys():
            if not only_files:
                res.append(jsn[tab][key])

            elif only_files and jsn[tab]["path"] is not None:
                res.append(jsn[tab][key])

        return res

    def check_tab_paths_exist(self) -> None:
        for i, widget in enumerate(self.get_all_widgets()):
            if hasattr(widget, "get_full_path"):
                if not FileChecker.check_exist(widget.get_full_path()):
                    del self.__tabs[i]
                    self.removeTab(i)

    def update_all_tabs_font(self) -> None:
        for widget in self.get_all_widgets():
            if hasattr(widget, "update_font"):
                widget.update_font()

    def update_all_tabs_settings(self) -> None:
        for widget in self.get_all_widgets():
            if hasattr(widget, "update_settings"):
                widget.update_settings()

    def find_by_path(self, __path: str):
        for widget in self.get_info_tabs(key="widget", only_files=True):
            if widget.get_full_path() == __path:
                return widget

    def get_all_widgets(self) -> list[Any]:
        return [self.widget(i) for i in range(self.count())]

    def get_all_paths(self):
        return self.get_info_tabs(key="path", only_files=True)

    def get_current_path(self) -> str:
        if hasattr(self.currentWidget(), "get_full_path"):
            return self.currentWidget().get_full_path()
        else:
            return ""  # it's need to remove exception

    def __update_indexes(self) -> None:
        for tab in self.__tabs:
            tab.index = self.indexOf(tab.widget)

            if tab.index == -1: self.__tabs.remove(tab)

        self.__tabs.sort(key=lambda t: t.index)

    def removeTab(self, __index: int):
        del self.__tabs[__index]
        super().removeTab(__index)

        if self.count() == 0:  # add welcome screen tab if tab bar is clear
            self.add_tab(Tab("Welcome!", WelcomeScreen(), IconPaths.SystemIcons.WELCOME))

        self.__update_indexes()

    def add_tab(self, tab: Tab):
        if tab.path is None and hasattr(tab.widget, "get_full_path"):
            tab.path = tab.widget.get_full_path()

        tab.index = len(self.__tabs)

        if tab.path not in self.get_all_paths():
            super().addTab(tab.widget, tab.title)
            self.__tabs.append(tab)
        else:
            self.setCurrentWidget(self.find_by_path(tab.path))

        if tab.icon is not None:
            self.setTabIcon(self.indexOf(tab.widget), tab.icon)
