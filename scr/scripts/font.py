from PySide6.QtGui import QFontDatabase, QFont


class Font:
    @staticmethod
    def get_all_font_families() -> list[str]:
        return QFontDatabase.families()

    @staticmethod
    def get_font_by_path(__path: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        __id = QFontDatabase.addApplicationFont(__path)
        families = QFontDatabase.applicationFontFamilies(__id)

        font = QFont(families[0], __size, 1, __italic)
        font.setBold(__bold)

        return font

    @staticmethod
    def get_system_font(__family: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        font = QFont(__family, __size, 1, __italic)
        font.setBold(__bold)

        return font