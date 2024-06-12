from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidget, QListWidgetItem

from scr.scripts.tools.file import FileLoader


class ListChanger(QListWidget):
    """
    Custom QListWidget for managing lists with interactive features.

    Methods:
    - __init__(*__values) -> None
        - Initializes the ListChanger with initial values.

    - use() -> None
        - Override this method to define custom behavior when an item is used.

    - keyPressEvent(event)
        - Handles key events for navigation and item selection.

    - set_items(*__values: str) -> None
        - Clears the list and sets new items.

    - add_items(*__labels: str) -> None
        - Adds additional items to the list.

    - get_item_by_text(__label: str)
        - Returns the QListWidgetItem with the specified label.

    - get_items() -> list[QListWidgetItem]
        - Returns a list of all QListWidgetItems in the list.

    - get_current_item()
        - Returns the current selected item.

    Attributes:
    - No specific attributes documented.

    Signals:
    - No specific signals documented.
    """

    def __init__(self, *__values) -> None:
        super().__init__()

        self.setStyleSheet(self.styleSheet() + FileLoader.load_style("scr/interface/abstract/styles/list_changer.css"))

        self.addItems([*__values])

    def use(self) -> None:
        # Override this method

        ...

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Down and self.currentRow() + 1 < self.count():
            self.setCurrentRow(self.currentRow() + 1)

        elif event.key() == Qt.Key.Key_Up and self.currentRow() > 0:
            self.setCurrentRow(self.currentRow() - 1)

        elif event.key() == Qt.Key.Key_Return:
            self.use()

        else:
            super().keyPressEvent(event)

    def set_items(self, *__values: str) -> None:
        self.clear()
        self.addItems([*__values])

    def add_items(self, *__labels: str) -> None:
        self.addItems([*__labels])

    def get_item_by_text(self, __label: str):
        for i in range(self.count()):
            if self.item(i).text() == __label:
                return self.item(i)

    def get_items(self) -> list[QListWidgetItem]:
        return [self.item(i) for i in range(self.count())]

    def get_current_item(self):
        return self.currentItem()