from PySide6.QtWidgets import QListWidget, QVBoxLayout
from PySide6.QtCore import Qt

from scr.scripts.tools.file import FileLoader


class ListChanger(QListWidget):
    def __init__(self, __parent = None, *__values) -> None:
        super().__init__(__parent)

        self.setStyleSheet(self.styleSheet() + FileLoader.load_style("scr/interface/abstract/styles/list_changer.css"))

        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.addItems([*__values])

    def accept(self) -> None:
        # Override this method

        ...

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Down and self.currentRow() + 1 < self.count():
            self.setCurrentRow(self.currentRow() + 1)

        elif event.key() == Qt.Key.Key_Up and self.currentRow() > 0:
            self.setCurrentRow(self.currentRow() - 1)

        elif event.key() == Qt.Key.Key_Return:
            self.accept()

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

    def get_current_item(self):
        return self.currentItem()