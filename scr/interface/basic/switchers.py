from PySide6.QtWidgets import QPushButton, QSpinBox, QSplitter
from PySide6.QtCore import Qt

from scr.scripts import FileLoader


class Splitter(QSplitter):
    def __init__(self, __orientation: str, *, parent=None) -> None:
        if __orientation == "horizontal": super().__init__(Qt.Orientation.Horizontal, parent)
        elif __orientation == "vertical": super().__init__(Qt.Orientation.Vertical, parent)

        self.setStyleSheet(FileLoader.load_style("scr/styles/switchers.css"))