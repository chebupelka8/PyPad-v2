from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout
from scr.scripts.tools.file import FileLoader


class ShellFrame(QFrame):
    def __init__(self, __parent = None, width: int = 600, height: int = 400):
        super().__init__(__parent)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/shell.css"))
        self.setObjectName("shell")

    def add_widget(self, __widget) -> None:
        self.mainLayout.addWidget(__widget)