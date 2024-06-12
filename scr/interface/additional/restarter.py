from scr.interface.abstract import Dialog
from scr.scripts.utils import restart_application


class Restarter(Dialog):
    def __init__(self, __parent) -> None:
        """
        Initializes the Restarter dialog with a message and title.

        Parameters:
        __parent (QWidget): Parent widget for the dialog.
        """

        super().__init__(__parent, "Do you want to restart the IDE to save the changes", "Restart")

        self.setMinimumWidth(500)
        self.__command = None

    def set_command_after_restart(self, __command):
        """
        Sets the command to be executed after the restart.

        Parameters:
        __command (function): The command to be executed after the restart.
        """

        self.__command = __command

    def accept(self):
        """
        Executes the stored command and resets it after one use.
        Restarts the application after executing the command.
        """

        self.__command()
        self.__command = None  # reset command

        restart_application()