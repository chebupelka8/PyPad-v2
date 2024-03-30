from PySide6.QtWidgets import QSplitter, QComboBox, QSpinBox
from PySide6.QtCore import Qt, QSize

from scr.scripts.tools.file import FileLoader


class Splitter(QSplitter):
    def __init__(self, __orientation: str, *, parent=None) -> None:
        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/splitter.css"))

    def addWidget(self, widget):
        super().addWidget(widget)
        self.setCollapsible(self.indexOf(widget), False)


class DropDownMenu(QComboBox):
    def __init__(self, *__values: str, width: int = 200, height: int = 30) -> None:
        super().__init__()

        self.setFixedSize(QSize(width, height))

        self.__values = [*__values]
        self.addItems(self.__values)

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/drop_down_menu.css"))

    def set_items(self, *__values: str) -> None:
        self.__values = [*__values]
        self.addItems(self.__values)


class DigitalEntry(QSpinBox):
    def __init__(self, __range: tuple[int, int]) -> None:
        super().__init__()

        self.setRange(*__range)
        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/digital_entry.css"))