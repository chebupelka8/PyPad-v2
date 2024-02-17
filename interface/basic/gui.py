from PySide6.QtWidgets import (
    QLabel,
)
from scr.scripts import Font


class UiTitles:

    @staticmethod
    def title(__text: str) -> QLabel:
        label = QLabel(__text)
        label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 17, True))

        return label

    @staticmethod
    def subtitle(__text: str) -> QLabel:
        label = QLabel(__text)
        label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 14, False))

        return label

    @staticmethod
    def description(__text: str) -> QLabel:
        label = QLabel(__text)
        label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", 10))

        return label
