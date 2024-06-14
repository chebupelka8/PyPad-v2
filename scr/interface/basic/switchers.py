import os.path

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QWidget,
)

from scr.scripts.tools.file import FileDialog, FileLoader

from .buttons import DefaultButton


class Splitter(QSplitter):
    """
    Custom QSplitter widget for managing layout splitting.

    Methods:
    - __init__(__orientation: str, *, parent=None): None - Initializes the splitter with a specified orientation.
    - addWidget(widget): None - Adds a widget to the splitter and sets it as non-collapsible.
    """

    def __init__(self, __orientation: str, *, parent=None) -> None:
        if __orientation == "horizontal":
            super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical":
            super().__init__(Qt.Orientation.Vertical, parent)

        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/splitter.css")
        )

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
        self.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.__values = [*__values]
        self.addItems(self.__values)

        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/drop_down_menu.css")
        )

    def set_items(self, *__values: str) -> None:
        self.__values = [*__values]
        self.addItems(self.__values)


class Entry(QLineEdit):
    """
    Custom QLineEdit widget for text entry.

    Methods:
    - __init__(__placed: str, placeholder: str = "", width: int = 200, height: int = 25): None - Initializes the text entry with default text and placeholder.
    """

    def __init__(
        self,
        __placed: str = "",
        placeholder: str = "",
        width: int = 200,
        height: int = 25,
    ) -> None:
        super().__init__()

        self.setFixedSize(QSize(width, height))
        self.setText(__placed)
        self.setPlaceholderText(placeholder)

        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/entry.css")
        )


class DigitalEntry(QSpinBox):
    """
    Custom QSpinBox widget for entering digital values.

    Methods:
    - __init__(__range: tuple[int, int], width: int = 30, height: int = 25, show_buttons: bool = False): None - Initializes the digital entry with a specified range, width, height, and button display.
    """

    def __init__(
        self,
        __range: tuple[int, int],
        width: int = 30,
        height: int = 25,
        show_buttons: bool = False,
    ) -> None:
        super().__init__()

        self.setFixedSize(QSize(width, height))
        if not show_buttons:
            self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.setRange(*__range)
        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/digital_entry.css")
        )


class PathEntry(QWidget):
    """
    Custom QLineEdit widget for entering path to file and directories.

    Methods:
    - __init__(self, __placed: str, placeholder: str = "", width: int = 400, height: int = 25): None - Initializes the path entry with default text and placeholder.
    - get_entry(self): Entry - returns the Entry widget.
    - set_path(self, __path: str, only_existing: bool = True): None if only_existing is True and path is not exist this path won't be pasted.

    Notes:
    - This widget includes Entry and PushButton to specify the path to your file or directory
    """

    def __init__(
        self,
        __placed: str = "",
        placeholder: str = "",
        width: int = 400,
        height: int = 25,
    ) -> None:
        super().__init__()

        self.setObjectName("path-entry-widget")
        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/path_entry.css")
        )

        self.mainLayout = QHBoxLayout()

        self.pathEntry = Entry(__placed, placeholder, width, height)

        self.specifyPathBtn = DefaultButton("...", width=25)
        self.specifyPathBtn.clicked.connect(
            lambda: self.set_path(FileDialog.get_open_file_name())
        )

        self.mainLayout.addWidget(self.pathEntry)
        self.mainLayout.addWidget(self.specifyPathBtn)
        self.mainLayout.addItem(
            QSpacerItem(
                20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
            )
        )
        self.setLayout(self.mainLayout)

    def set_path(self, __path: str, only_existing: bool = True) -> None:
        if only_existing and os.path.exists(__path):
            self.pathEntry.setText(__path)
            return

        self.pathEntry.setText(__path)

    def get_entry(self) -> Entry:
        return self.pathEntry
