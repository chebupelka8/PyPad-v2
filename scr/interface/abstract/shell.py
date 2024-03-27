from PySide6.QtWidgets import QFrame
from scr.scripts.tools.file import FileLoader


class ShellFrame(QFrame):
    def __init__(self, __parent, width: int = 600, height: int = 400):
        super().__init__(__parent)

        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/shell.qss"))
        self.setObjectName("shell")