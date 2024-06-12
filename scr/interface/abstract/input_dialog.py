from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QVBoxLayout)

from scr.scripts.tools.file import FileLoader

from .windows import DialogWindow


class InputDialog(DialogWindow):
    """
            Custom dialog window for input with message and buttons.

            Methods:
            - __init__(
                __parent, __message: str,
                pasted_text: str = "", place_holder_text: str = "",
                accept_title: str = "Ok", reject_title: str = "Cancel"
            ): None
                - Initializes the input dialog with specified parameters.
                - __parent: Parent widget for the dialog.
                - __message: Message displayed in the dialog.
                - pasted_text: Default text in the input line.
                - place_holder_text: Placeholder text for the input line.
                - accept_title: Title for the accept button (default: "Ok").
                - reject_title: Title for the reject button (default: "Cancel").

            Attributes:
            - mainLayout: QVBoxLayout - Main layout of the dialog.
            - buttonLayout: QHBoxLayout - Layout for buttons.
            - inputLine: QLineEdit - Input line for user input.
            - acceptBtn: QPushButton - Button to accept input.
            - rejectBtn: QPushButton - Button to reject input.

            Signals:
            - accept(): Signal emitted when the accept button is clicked.
            - reject(): Signal emitted when the reject button is clicked.
            """

    def __init__(
            self, __parent,
            __message: str,
            pasted_text: str = "", place_holder_text: str = "",
            accept_title: str = "Ok", reject_title: str = "Cancel"
    ) -> None:
        super().__init__(__parent)

        self.setStyleSheet(
            self.styleSheet() + FileLoader.load_style("scr/interface/abstract/styles/dialog_buttons.css")
        )

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.mainLayout.addWidget(
            QLabel(__message), alignment=Qt.AlignmentFlag.AlignCenter
        )

        # input line
        self.inputLine = QLineEdit()
        self.inputLine.setText(pasted_text)
        self.inputLine.setPlaceholderText(place_holder_text)
        self.mainLayout.addWidget(self.inputLine)

        # buttons
        self.mainLayout.addLayout(self.buttonLayout)

        self.acceptBtn = QPushButton(accept_title)
        self.acceptBtn.setObjectName("accept-btn")
        self.rejectBtn = QPushButton(reject_title)
        self.rejectBtn.setObjectName("reject-btn")

        self.acceptBtn.clicked.connect(self.accept)
        self.rejectBtn.clicked.connect(self.reject)

        self.buttonLayout.addWidget(self.acceptBtn, alignment=Qt.AlignmentFlag.AlignRight)
        self.buttonLayout.addWidget(self.rejectBtn, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.mainLayout)