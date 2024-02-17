from scr.scripts import FileLoader, restart_application, ThemeManager
from scr.interface.additional import Dialog, ListChanger


class Restarter(Dialog):
    def __init__(self, __parent) -> None:
        super().__init__(__parent, "Do you want to restart the IDE to save the changes", "Restart")

        self.setMinimumWidth(500)
        self.__command = None

    def set_command_after_restart(self, __command):
        """This command will be reset after one use"""

        self.__command = __command

    def accept(self):
        self.__command()
        self.__command = None  # reset command

        restart_application()


class ThemeChanger(ListChanger):
    def __init__(self, __parent, restarter: Restarter) -> None:
        super().__init__(__parent)

        self.restarter = restarter
        self.listWidget.itemClicked.connect(self.accept)

    def change_theme(self, __name: str) -> None:
        self.close()

        ThemeManager.set_current_theme_by_name(__name)

        self.restarter.set_command_after_restart(ThemeManager.save)
        self.restarter.show()

    def show(self):
        super().show()
        self.listWidget.setCurrentItem(self.get_item_by_text(ThemeManager.get_current_theme_name()))

    def accept(self):
        self.change_theme(self.get_current_item().text())
