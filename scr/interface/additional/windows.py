from PySide6.QtWidgets import (
    QVBoxLayout, QListWidget
)
from PySide6.QtCore import Qt

from ..abstract import TransparentDialogWindow

from scr.scripts.tools.file import FileLoader


class ListChanger(TransparentDialogWindow):
    def __init__(self, __parent, *__values, width: int = 200, height: int = 400) -> None:
        super().__init__(__parent)

        self.setStyleSheet(self.styleSheet() + FileLoader.load_style("scr/interface/additional/styles/gui.css"))

        self.setMinimumSize(width, height)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.mainLayout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listWidget.addItems([*__values])
        self.mainLayout.addWidget(self.listWidget)

        self.setLayout(self.mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Down and self.listWidget.currentRow() + 1 < self.listWidget.count():
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)

        elif event.key() == Qt.Key.Key_Up and self.listWidget.currentRow() > 0:
            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)

        elif event.key() == Qt.Key.Key_Return:
            self.accept()

        else:
            super().keyPressEvent(event)

    def set_items(self, *__values: str) -> None:
        self.listWidget.clear()
        self.listWidget.addItems([*__values])

    def add_items(self, *__labels: str) -> None:
        self.listWidget.addItems([*__labels])

    def get_item_by_text(self, __label: str):
        for i in range(self.listWidget.count()):

            if self.listWidget.item(i).text() == __label:
                return self.listWidget.item(i)

    def show(self):
        super().show()

    def get_current_item(self):
        return self.listWidget.currentItem()
