from scr.interface.additional import ListChanger


class TabsSwitcher(ListChanger):
    def __init__(self, parent) -> None:
        super().__init__(parent, width=500, height=700)

        self.__items = []
        self.listWidget.currentRowChanged.connect(self.__changed)

    def __changed(self, __index: int) -> None:
        current_item = self.listWidget.currentItem()
        if current_item is None: return

        if self.__items[__index].is_file():
            current_item.setText(f'{current_item.text()}    {self.__items[__index].path}')

        self.__reset_titles()

    def __reset_titles(self) -> None:
        for tab in self.__items:
            if tab.index != self.listWidget.currentRow():
                self.listWidget.item(tab.index).setText(tab.title)

    def set_items(self, items: list) -> None:
        self.__items = items
        self.listWidget.clear()

        for i, item in enumerate(items):
            self.listWidget.addItem(item.title)
            self.listWidget.item(item.index).setIcon(item.icon)

    def open_connect(self, __command) -> None:
        self.accept = lambda: self.__accept(__command)
        self.listWidget.itemClicked.connect(self.accept)

    def __accept(self, __command) -> None:
        __command(self.__items[self.listWidget.currentRow()].index)
        super().accept()
