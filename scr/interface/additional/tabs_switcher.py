from scr.interface.abstract import ListChanger, TransparentDialogWindow, ShellFrame

import os


class TabsSwitcher(ListChanger):
    def __init__(self, __parent) -> None:
        super().__init__(__parent)

        self.__parent = __parent

        self.__items = []
        self.currentRowChanged.connect(self.__changed)

    @staticmethod
    def __to_shorter_path(__path: str) -> str:
        __path = os.path.normpath(__path)
        arr = __path.split("\\")

        if len(arr) <= 3:
            return "\\".join(["...", *arr])
        else:
            return "\\".join(["...", *arr[-3:]])

    def __changed(self, __index: int) -> None:
        current_item = self.currentItem()
        if current_item is None: return

        if self.__items[__index].is_file():
            current_item.setText(f'{current_item.text()}{" " * 25}{self.__to_shorter_path(self.__items[__index].path)}')

        self.__reset_titles()

    def __reset_titles(self) -> None:
        # There is unknown error and I don't know why this error appears
        # Probably this bug have been fixed

        for tab in self.__items:
            if tab.index != self.currentRow():
                self.item(tab.index).setText(tab.title)

    def set_items(self, items: list) -> None:
        self.__items = items
        self.clear()

        for i, item in enumerate(items):
            self.addItem(item.title)
            self.item(item.index).setIcon(item.icon)

    def set_current_index(self, __index: int) -> None:
        self.setCurrentRow(__index)

    def open_connect(self, __command) -> None:
        self.use = lambda: self.__accept(__command)
        self.itemClicked.connect(self.use)

    def __accept(self, __command) -> None:
        self.__parent.accept()
        __command(self.__items[self.currentRow()].index)


class TabsSwitcherWindow(TransparentDialogWindow):
    def __init__(self, __parent) -> None:
        super().__init__(__parent)

        self.tabSwitcher = TabsSwitcher(self)
        self.add_widget(self.tabSwitcher)

    def show_window(self, __items: list, current: int, __command) -> None:
        self.tabSwitcher.set_items(__items)
        self.tabSwitcher.set_current_index(current)
        self.tabSwitcher.open_connect(__command)
        self.show()
