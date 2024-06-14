from .abstract_action_menu import AbstractActionMenu


class SettingsActionMenu(AbstractActionMenu):
    def __init__(self, parent=None) -> None:
        super().__init__(parent, width=200)

        self.add_action("Interpreter Settings...")
        self.add_action("Open Settings...", shortcut="ctrl+,")
        self.add_action("Themes...", shortcut="ctrl+t")
