from scr.scripts.utils import restart_application
from scr.scripts.theme import ThemeManager

from PySide6.QtWidgets import QLabel

# from scr.interface.additional import ListChanger  # need replace

from scr.interface.abstract import Dialog, ListChanger, ShellFrame, TransparentDialogWindow


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
    def __init__(self, restarter: Restarter) -> None:
        super().__init__()

        self.restarter = restarter
        self.itemClicked.connect(self.use)

    def change_theme(self, __name: str) -> None:
        # self.close()

        ThemeManager.set_current_theme_by_name(__name)

        self.restarter.set_command_after_restart(ThemeManager.save)
        self.restarter.show()

    def open(self):
        self.setCurrentItem(self.get_item_by_text(ThemeManager.get_current_theme_name()))

    def use(self):
        self.change_theme(self.get_current_item().text())


class ThemeChangerWindow(TransparentDialogWindow):
    def __init__(self, __parent, __restarter: Restarter) -> None:
        super().__init__(__parent)

        self.themeChanger = ThemeChanger(__restarter)
        self.add_widget(QLabel("Themes..."))
        self.add_widget(self.themeChanger)

    def accept(self):
        self.themeChanger.use()

    def show(self):
        super().show()
        self.themeChanger.open()
