from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from scr.interface.basic import DialogButton, Text

from .windows import DialogWindow


class Dialog(DialogWindow):
    """
    Custom dialog window for displaying messages with buttons.

    Methods:
    - __init__(
        __parent, __message: str,
        accept_title: str = "Ok", reject_title: str = "Cancel"
    ): None
        - Initializes the dialog with specified parameters.
        - __parent: Parent widget for the dialog.
        - __message: Message displayed in the dialog.
        - accept_title: Title for the accept button (default: "Ok").
        - reject_title: Title for the reject button (default: "Cancel").

    Attributes:
    - mainLayout: QVBoxLayout - Main layout of the dialog.
    - buttonLayout: QHBoxLayout - Layout for buttons.
    - acceptBtn: DialogButton - Button to accept the dialog.
    - rejectBtn: DialogButton - Button to reject the dialog.

    Signals:
    - accept(): Signal emitted when the accept button is clicked.
    - reject(): Signal emitted when the reject button is clicked.
    """

    def __init__(self, __parent, __message: str, accept_title: str = "Ok", reject_title: str = "Cancel") -> None:
        super().__init__(__parent)

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.mainLayout.addWidget(
            Text.label(__message, "CascadiaMono.ttf", 9), alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.mainLayout.addLayout(self.buttonLayout)

        self.acceptBtn = DialogButton(accept_title, "accept")
        self.rejectBtn = DialogButton(reject_title, "reject")

        self.acceptBtn.clicked.connect(self.accept)
        self.rejectBtn.clicked.connect(self.reject)

        self.buttonLayout.addWidget(self.acceptBtn, alignment=Qt.AlignmentFlag.AlignRight)
        self.buttonLayout.addWidget(self.rejectBtn, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.mainLayout)
