from PySide6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout
from scr.scripts.tools.file import FileLoader

from typing import Optional, Union


class ShellFrame(QFrame):
    def __init__(self, __parent = None, shell_layout_type: str = "vertical",
                 width: int = 600, height: int = 400):
        super().__init__(__parent)

        if shell_layout_type == "vertical": self.mainLayout = QVBoxLayout()
        elif shell_layout_type == "horizontal": self.mainLayout = QHBoxLayout()

        self.setLayout(self.mainLayout)

        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/shell.css"))
        self.setObjectName("shell")

    def add_widget(self, __widget, stretch: Optional[int] = None) -> None:
        if stretch is not None:
            self.mainLayout.addWidget(__widget, stretch=stretch)
        else:
            self.mainLayout.addWidget(__widget)