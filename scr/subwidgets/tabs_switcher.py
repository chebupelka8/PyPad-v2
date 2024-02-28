from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout, QListWidget
)

from scr.interface.additional import ListChanger


class TabsSwitcher(ListChanger):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.__items = []

    def set_items(self, items: list) -> None:
        """

        :param items: List[ [title, w, icon, index], ... ]
        :return: None
        """

        self.__items = items
        self.listWidget.clear()

        for i, item in enumerate(items):
            self.listWidget.addItem(item[0])
            self.listWidget.item(i).setIcon(item[2])

    def open_connect(self, __command) -> None:
        self.listWidget.itemClicked.connect(lambda item: __command(item.text()))
