from .windows import DialogWindow

from PySide6.QtWidgets import (
    QHBoxLayout, QVBoxLayout
)
from PySide6.QtCore import Qt

from scr.interface.basic import DialogButton, Text


class Dialog(DialogWindow):
    def __init__(self, __parent, __message: str, accept_title: str = "Ok", reject_title: str = "Cancel") -> None:
        super().__init__(__parent)

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.mainLayout.addWidget(
            Text.label(__message, "cascadia mono", 9), alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.mainLayout.addLayout(self.buttonLayout)

        self.acceptBtn = DialogButton(accept_title, "accept")
        self.rejectBtn = DialogButton(reject_title, "reject")

        self.acceptBtn.clicked.connect(self.accept)
        self.rejectBtn.clicked.connect(self.reject)

        self.buttonLayout.addWidget(self.acceptBtn, alignment=Qt.AlignmentFlag.AlignRight)
        self.buttonLayout.addWidget(self.rejectBtn, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.mainLayout)
