from PySide6.QtWidgets import QSplitter
from PySide6.QtCore import Qt

from scr.scripts.tools.file import FileLoader


class Splitter(QSplitter):
    def __init__(self, __orientation: str, *, parent=None) -> None:
        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        self.setStyleSheet(FileLoader.load_style("scr/interface/basic/styles/switchers.css"))

    def addWidget(self, widget):
        super().addWidget(widget)
        self.setCollapsible(self.indexOf(widget), False)