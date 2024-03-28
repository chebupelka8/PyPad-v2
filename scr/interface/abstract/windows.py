from PySide6.QtWidgets import QDialog, QHBoxLayout, QWidget
from PySide6.QtCore import Qt

from scr.scripts.tools.file import FileLoader
from .shell import ShellFrame


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

        self.shell = ShellFrame(self)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.shell)
        self.setLayout(self.mainLayout)

    def add_widget(self, widget) -> None:
        self.shell.add_widget(widget)

    def close(self):
        self.shell.close()
        self.close()

    # def set_central_widget(self, __widget) -> None:
    #     self.mainLayout.addWidget(__widget)