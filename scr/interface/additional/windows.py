from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QVBoxLayout, QLabel,
    QPushButton, QLineEdit, QListWidget, QFrame
)
from PySide6.QtCore import Qt

from scr.scripts import FileLoader

from typing import Any


class DialogWindow(QDialog):
    def __init__(self, __parent: Any = None, *, frameless: bool = True) -> None:
        if frameless: super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)
        else: super().__init__(__parent)

        self.setStyleSheet(FileLoader.load_style("scr/styles/ui.css"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)


class TransparentDialogWindow(DialogWindow):
    def __init__(self, __parent: Any = None, *, frameless: bool = True) -> None:
        super().__init__(__parent, frameless=frameless)

        self.setAttribute(Qt.WA_TranslucentBackground)


class Dialog(DialogWindow):
    def __init__(self, __parent, __message: str, accept_title: str = "Ok", reject_title: str = "Cancel") -> None:
        super().__init__(__parent)

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.mainLayout.addWidget(
            QLabel(__message), alignment=Qt.AlignmentFlag.AlignCenter
        )
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:
            self.accept()

        else:
            super().keyPressEvent(event)


class InputDialog(DialogWindow):
    def __init__(
            self, __parent,
            __message: str,
            pasted_text: str = "", place_holder_text: str = "",
            accept_title: str = "Ok", reject_title: str = "Cancel"
    ) -> None:
        super().__init__(__parent)

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


class ListChanger(TransparentDialogWindow):
    def __init__(self, __parent, *__values, width: int = 200, height: int = 400) -> None:
        super().__init__(__parent)

        self.setMinimumSize(width, height)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.mainLayout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.listWidget.addItems([*__values])
        self.mainLayout.addWidget(self.listWidget)

        self.setLayout(self.mainLayout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Down and self.listWidget.currentRow() + 1 < self.listWidget.count():
            self.listWidget.setCurrentRow(self.listWidget.currentRow() + 1)

        elif event.key() == Qt.Key.Key_Up and self.listWidget.currentRow() > 0:
            self.listWidget.setCurrentRow(self.listWidget.currentRow() - 1)

        elif event.key() == Qt.Key.Key_Return:
            self.accept()

        else:
            super().keyPressEvent(event)

    def add_items(self, *__labels: str) -> None:
        self.listWidget.clear()
        self.listWidget.addItems([*__labels])

    def get_item_by_text(self, __label: str):
        for i in range(self.listWidget.count()):

            if self.listWidget.item(i).text() == __label:
                return self.listWidget.item(i)

    def show(self):
        super().show()

    def get_current_item(self):
        return self.listWidget.currentItem()


class AbstractWindow(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/styles/ui.css"))
        self.setObjectName("abstract-window")
