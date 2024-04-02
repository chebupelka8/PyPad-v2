from PySide6.QtWidgets import QSplitter, QComboBox, QSpinBox, QLineEdit
from PySide6.QtCore import Qt, QSize

from scr.scripts.tools.file import FileLoader


class Splitter(QSplitter):
    """
    Custom QSplitter widget for managing layout splitting.

    Methods:
    - __init__(__orientation: str, *, parent=None): None - Initializes the splitter with a specified orientation.
    - addWidget(widget): None - Adds a widget to the splitter and sets it as non-collapsible.
    """

    def __init__(self, __orientation: str, *, parent=None) -> None:
        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/splitter.css"))

    def addWidget(self, widget):
        super().addWidget(widget)
        self.setCollapsible(self.indexOf(widget), False)


class DropDownMenu(QComboBox):
    """
    Custom QComboBox widget for displaying a drop-down menu.

    Methods:
    - __init__(*__values: str, width: int = 200, height: int = 25): None - Initializes the drop-down menu with specified values, width, and height.
    - set_items(*__values: str): None - Sets the items in the drop-down menu.
    """

    def __init__(self, *__values: str, width: int = 200, height: int = 25) -> None:
        super().__init__()

        self.setFixedSize(QSize(width, height))

        self.__values = [*__values]
        self.addItems(self.__values)

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/drop_down_menu.css"))

    def set_items(self, *__values: str) -> None:
        self.__values = [*__values]
        self.addItems(self.__values)


class Entry(QLineEdit):
    """
    Custom QLineEdit widget for text entry.

    Methods:
    - __init__(__placed: str, placeholder: str = "", width: int = 200, height: int = 25): None - Initializes the text entry with default text and placeholder.
    """

    def __init__(self, __placed: str, placeholder: str = "", width: int = 200, height: int = 25) -> None:
        super().__init__()

        self.setFixedSize(QSize(width, height))
        self.setText(__placed)
        self.setPlaceholderText(placeholder)

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/entry.css"))


class DigitalEntry(QSpinBox):
    """
    Custom QSpinBox widget for entering digital values.

    Methods:
    - __init__(__range: tuple[int, int], width: int = 30, height: int = 25, show_buttons: bool = False): None - Initializes the digital entry with a specified range, width, height, and button display.
    """

    def __init__(self, __range: tuple[int, int], width: int = 30, height: int = 25, show_buttons: bool = False) -> None:
        super().__init__()

        self.setFixedSize(QSize(width, height))
        if not show_buttons: self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.setRange(*__range)
        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/digital_entry.css"))