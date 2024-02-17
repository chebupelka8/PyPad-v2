from PySide6.QtWidgets import QListWidget, QWidget, QHBoxLayout

from scr.scripts import FileLoader, EditorFontManager, Font


class Completer(QListWidget):
    def __init__(self) -> None:
        super().__init__()

        # font setup
        self.__main_font = Font.get_system_font(
            EditorFontManager.get_current_family(), EditorFontManager.get_current_font_size() * 0.8
        )
        self.setFont(self.__main_font)

        self.setObjectName("completer")

    def set_items(self, __items: list[str]) -> None:
        self.clear()
        self.addItems(__items)


class WindowCompleter(QWidget):
    def __init__(self, __parent) -> None:
        super().__init__(__parent)

        self.setStyleSheet(
            FileLoader.load_style("scr/styles/completer.css")
        )
        self.setObjectName("window-completer")
        self.setMinimumWidth(400)

        self.completer = Completer()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.completer)

        self.setLayout(self.mainLayout)

    def set_items(self, __items: list[str]) -> None:
        self.completer.set_items(__items)

    def clear(self) -> None:
        self.completer.clear()
