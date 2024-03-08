from PySide6.QtWidgets import QLabel

from scr.scripts.font import Font


class GuiText:

    @staticmethod
    def label(__text: str, font_family: str, font_size: int, bold: bool = False, italic: bool = False) -> QLabel:
        label = QLabel(__text)
        label.setFont(Font.get_system_font(font_family, font_size, bold, italic))

        return label