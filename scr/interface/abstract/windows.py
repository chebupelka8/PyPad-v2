from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

from scr.scripts.tools.file import FileLoader


class DialogWindow(QDialog):
    def __init__(self, __parent, *, frameless: bool = True) -> None:
        if frameless: super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)
        else: super().__init__(__parent)

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/dialog.css"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)


class TransparentDialogWindow(DialogWindow):
    def __init__(self, __parent, *, frameless: bool = True) -> None:
        super().__init__(__parent, frameless=frameless)

        self.setAttribute(Qt.WA_TranslucentBackground)