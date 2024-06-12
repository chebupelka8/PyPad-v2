from PySide6.QtGui import QColor, QFont, QTextCharFormat


class TextCharCreator:
    @staticmethod
    def create_char_format(
        __color: str, italic: bool = False, bold: bool = False
    ) -> QTextCharFormat:
        res = QTextCharFormat()
        res.setForeground(QColor(__color))
        res.setFontItalic(italic)
        if bold:
            res.setFontWeight(QFont.Bold)

        return res

    @classmethod
    def create_char_format_background(
        cls, __bg_color: str, italic: bool = False, bold: bool = False
    ):
        res = QTextCharFormat()
        res.setForeground(QColor(__bg_color))
        res.setFontItalic(italic)
        if bold:
            res.setFontWeight(QFont.Bold)

        return res
