from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QListWidget
)

from scr.interface.additional import ListChanger


class TabsSwitcher(ListChanger):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def open_connect(self, __command) -> None:
        self.listWidget.itemClicked.connect(lambda item: __command(item.text()))
