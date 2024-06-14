from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMenu

from scr.scripts.tools.file import FileLoader


class AbstractActionMenu(QMenu):
    def __init__(self, parent=None, width: int = 150) -> None:
        super().__init__(parent)

        self.setFixedWidth(width)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.NoDropShadowWindowHint)
        self.setStyleSheet(
            FileLoader.load_style("scr/subwidgets/styles/action_menu.css")
        )

    def add_action(
        self, __title: str, path_to_icon: str | None = None, shortcut: Any | None = None
    ):
        action = QAction(__title, self)
        if shortcut is not None:
            action.setShortcut(shortcut)
        if path_to_icon is not None:
            action.setIcon(QIcon(path_to_icon))

        self.addAction(action)

    def get_action_by_title(self, __title: str) -> QAction | None:
        for i in self.actions():
            if i.text() == __title:
                return i

    def connect_by_title(self, __title: str, __command):
        self.get_action_by_title(__title).triggered.connect(__command)

    def show(self):
        self.popup(self.cursor().pos())
        super().show()
