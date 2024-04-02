from scr.interface.abstract import ListChanger, TransparentDialogWindow
from scr.interface.basic import Text

import os


class TabsSwitcher(ListChanger):
    def __init__(self, __parent) -> None:
        """
        Initializes the TabsSwitcher object.

        Parameters:
        __parent (QWidget): Parent widget for the TabsSwitcher.
        """

        super().__init__(__parent)

        self.__parent = __parent

        self.__items = []
        self.currentRowChanged.connect(self.__changed)

    @staticmethod
    def __to_shorter_path(__path: str) -> str:
        """
        Converts a full path to a shorter representation.

        Parameters:
        __path (str): Full path to be converted.

        Returns:
        str: Shortened path representation.
        """

        __path = os.path.normpath(__path)
        arr = __path.split("\\")

        if len(arr) <= 3:
            return "\\".join(["...", *arr])
        else:
            return "\\".join(["...", *arr[-3:]])

    def __changed(self, __index: int) -> None:
        """
        Handles the change in the selected tab.

        Parameters:
        __index (int): Index of the selected tab.
        """

        current_item = self.currentItem()
        if current_item is None: return

        if self.__items[__index].is_file():
            current_item.setText(f'{current_item.text()}{" " * 25}{self.__to_shorter_path(self.__items[__index].path)}')

        self.__reset_titles()

    def __reset_titles(self) -> None:
        """
        Resets the titles of all tabs except the current one.
        """

        # There is unknown error and I don't know why this error appears
        # Probably this bug have been fixed

        for tab in self.__items:
            if tab.index != self.currentRow():
                self.item(tab.index).setText(tab.title)

    def set_items(self, items: list) -> None:
        """
        Sets the items for the TabsSwitcher.

        Parameters:
        items (list): List of items to be displayed as tabs.
        """

        self.__items = items
        self.clear()

        for i, item in enumerate(items):
            self.addItem(item.title)
            self.item(item.index).setIcon(item.icon)

    def set_current_index(self, __index: int) -> None:
        """
        Sets the current index of the selected tab.

        Parameters:
        __index (int): Index of the tab to be set as current.
        """

        self.setCurrentRow(__index)

    def open_connect(self, __command) -> None:
        """
        Connects a command to be executed on tab selection.

        Parameters:
        __command (function): Command to be executed on tab selection.
        """

        self.use = lambda: self.__accept(__command)
        self.itemClicked.connect(self.use)

    def __accept(self, __command) -> None:
        """
        Executes the command and accepts the selection.

        Parameters:
        __command (function): Command to be executed.
        """

        self.__parent.accept()
        __command(self.__items[self.currentRow()].index)


class TabsSwitcherWindow(TransparentDialogWindow):
    def __init__(self, __parent) -> None:
        """
        Initializes the TabsSwitcherWindow dialog.

        Parameters:
        __parent (QWidget): Parent widget for the dialog.
        """

        super().__init__(__parent, height=600, width=400)

        self.tabSwitcher = TabsSwitcher(self)
        self.add_widget(Text.label("Switcher...", "CascadiaMono.ttf", 9))
        self.add_widget(self.tabSwitcher)

    def show_window(self, __items: list, current: int, __command) -> None:
        """
        Displays the tab switcher window with specified items and current selection.

        Parameters:
        __items (list): List of items to be displayed as tabs.
        current (int): Index of the current selection.
        __command (function): Command to be executed on tab selection.
        """

        self.tabSwitcher.set_items(__items)
        self.tabSwitcher.set_current_index(current)
        self.tabSwitcher.open_connect(__command)
        self.show()
