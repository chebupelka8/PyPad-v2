from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

from scr.scripts.tools.file import FileLoader
from .shell import ShellFrame

from typing import Optional, Union


class DialogWindow(QDialog):
    def __init__(self, __parent, *, frameless: bool = True, keyboard_include: bool = True) -> None:
        if frameless: super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)
        else: super().__init__(__parent)

        self.__keyboard_include = keyboard_include

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/dialog.css"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

    def keyPressEvent(self, event):
        if self.__keyboard_include:
            if event.key() == Qt.Key.Key_Return:
                self.accept()

            elif event.key() == Qt.Key.Key_Escape:
                self.reject()

            else:
                super().keyPressEvent(event)

        else:
            super().keyPressEvent(event)


class TransparentDialogWindow(DialogWindow):
    def __init__(self, __parent, shell_layout_type: str = "vertical", *,
                 frameless: bool = True) -> None:
        super().__init__(__parent, frameless=frameless)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shell = ShellFrame(self, shell_layout_type)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.shell)
        self.setLayout(self.mainLayout)

    def add_widget(self, widget, stretch: Optional[int] = None) -> None:
        self.shell.add_widget(widget, stretch)

    def set_shell(self, __shell: ShellFrame) -> None:
        self.shell = __shell
