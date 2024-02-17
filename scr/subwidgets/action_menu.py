from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

from scr.scripts import FileLoader


class _ActionMenu(QMenu):
    def __init__(self, parent = None, width: int = 150) -> None:
        super().__init__(parent)

        self.setFixedWidth(width)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.NoDropShadowWindowHint)
        self.setStyleSheet(FileLoader.load_style("scr/styles/action_menu.css"))

    def add_action(self, __title: str, __path_to_icon: str | None = None):
        action = QAction(__title, self)
        # if __path_to_icon is not None: action.setIcon(QIcon(__path_to_icon))

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


class SettingsActionMenu(_ActionMenu):
    def __init__(self, parent = None) -> None:
        super().__init__(parent, width=200)

        self.add_action("Interpreter Settings...", "assets/icons/system_icons/interpreter.png")
        self.add_action("Open Settings...", "assets/icons/system_icons/settings.png")
        self.add_action("Themes...", "assets/icons/system_icons/themes.png")
