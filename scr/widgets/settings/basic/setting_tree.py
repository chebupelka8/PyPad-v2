from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import Qt

from scr.scripts.font import WorkbenchFontManager, Font


class SettingTree(QListWidget):
    def __init__(self):
        super().__init__()

        self.update_font()

        self.addItems(["General", "Editor", "Theme", "About"])
        self.setCurrentRow(0)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.__commands: dict = {}
        self.currentTextChanged.connect(self.__connection)

        WorkbenchFontManager.add_font_updater(self.update_font)

    def update_font(self) -> None:
        self.__main_font = Font.get_system_font(
            WorkbenchFontManager.get_current_family(), WorkbenchFontManager.get_current_font_size()
        )
        self.setFont(self.__main_font)

    def connect_by_title(self, __title: str, __command):
        try:
            self.__commands[__title] = __command

        except TypeError:
            ...

    def __connection(self, __text):
        if __text not in list(self.__commands.keys()): return

        self.__commands[__text]()