from PySide6.QtWidgets import QPushButton

from scr.scripts.tools.file import FileLoader


class PushButton(QPushButton):
    def __init__(self, __text: str) -> None:
        super().__init__()


class DialogButton(QPushButton):
    def __init__(self, __text: str, button_type: str = "accept") -> None:
        super().__init__(__text)

        if button_type == "accept": self.setObjectName("accept")
        elif button_type == "reject": self.setObjectName("reject")
        else: raise ValueError("Invalid button_type.")

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/dialog_buttons.css"))
