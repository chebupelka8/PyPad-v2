from PySide6.QtWidgets import QLabel

from scr.scripts.font import Font


class Text:
    @staticmethod
    def label(
        __text: str,
        font_family: str,
        font_size: int,
        bold: bool = False,
        italic: bool = False,
        color: str = "#ffffff",
        word_wrap: bool = False,
    ) -> QLabel:
        label = QLabel(__text)
        label.setStyleSheet(f"color: {color}")
        label.setWordWrap(word_wrap)
        label.setFont(Font.get_system_font(font_family, font_size, bold, italic))

        return label
