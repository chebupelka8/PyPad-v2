from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QPushButton

from scr.scripts.tools.file import FileLoader


class PushButton(QPushButton):
    def __init__(self, __text: str, width: int = 200, height: int = 25) -> None:
        super().__init__(__text)

        self.setFixedSize(QSize(width, height))
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)


class DefaultButton(PushButton):
    def __init__(self, __text: str, width: int = 200, height: int = 25):
        super().__init__(__text, width, height)

        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/default_button.css")
        )


class HighlightedButton(PushButton):
    def __init__(
        self,
        __text: str,
        color: str,
        border_color: str,
        width: int = 200,
        height: int = 25,
    ) -> None:
        super().__init__(__text, width, height)

        # ...


class DialogButton(PushButton):
    def __init__(
        self,
        __text: str,
        button_type: str = "accept",
        width: int = 200,
        height: int = 25,
    ) -> None:
        super().__init__(__text, width, height)

        if button_type == "accept":
            self.setObjectName("accept")
        elif button_type == "reject":
            self.setObjectName("reject")
        else:
            raise ValueError("Invalid button_type.")

        self.setStyleSheet(
            FileLoader.load_style("scr/interface/basic/styles/dialog_buttons.css")
        )
