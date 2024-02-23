from PySide6.QtGui import QFontDatabase, QFont

import os


class Font:
    @classmethod
    def get_all_font_families(cls) -> list[str]:
        system_fonts = QFontDatabase.families()

        return sorted(system_fonts + cls.__get_additional_fonts())

    @staticmethod
    def __get_additional_fonts() -> list[str]:
        res = []

        for font in os.listdir("assets/fonts"):
            res.append(font)

        return res

    @staticmethod
    def get_font_by_path(__path: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        __id = QFontDatabase.addApplicationFont(__path)
        families = QFontDatabase.applicationFontFamilies(__id)

        font = QFont(families[0], __size, 1, __italic)
        font.setBold(__bold)

        return font

    @classmethod
    def get_system_font(
            cls,
            __family: str,
            __size: int | float,
            __bold: bool = False,
            __italic: bool = False,
            check_exist_additional: bool = True
    ) -> QFont:
        if check_exist_additional and __family in cls.__get_additional_fonts():
            return cls.get_font_by_path(f"assets/fonts/{__family}", __size, __bold, __italic)

        font = QFont(__family, __size, 1, __italic)
        font.setBold(__bold)

        return font