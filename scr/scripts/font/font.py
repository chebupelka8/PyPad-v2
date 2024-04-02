from PySide6.QtGui import QFontDatabase, QFont

import os


class Font:
    @classmethod
    def get_all_font_families(cls) -> list[str]:
        """
        Get a list of all available font families, including system fonts and additional fonts.

        Returns:
            list[str]: A sorted list of all available font families.
        """

        system_fonts = QFontDatabase.families()

        return sorted(system_fonts + cls.__get_additional_fonts())

    @staticmethod
    def __get_additional_fonts() -> list[str]:
        """
        Get a list of additional fonts from the 'assets/fonts' directory.

        Returns:
            list[str]: A list of additional font file names.
        """

        res = []

        for font in os.listdir("assets/fonts"):
            res.append(font)

        return res

    @staticmethod
    def get_font_by_path(__path: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        """
        Load a font from a specific path with the given size, boldness, and italic style.

        Args:
            __path (str): The path to the font file.
            __size (int | float): The size of the font.
            __bold (bool, optional): Whether the font should be bold. Defaults to False.
            __italic (bool, optional): Whether the font should be italic. Defaults to False.

        Returns:
            QFont: The loaded font.
        """

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
        """
        Get a font by family name, size, boldness, and italic style, with an option to load additional fonts.

        Args:
            __family (str): The font family name.
            __size (int | float): The size of the font.
            __bold (bool, optional): Whether the font should be bold. Defaults to False.
            __italic (bool, optional): Whether the font should be italic. Defaults to False.
            check_exist_additional (bool, optional): Whether to check for additional fonts. Defaults to True.

        Returns:
            QFont: The requested font.
        """

        if check_exist_additional and __family in cls.__get_additional_fonts():
            return cls.get_font_by_path(f"assets/fonts/{__family}", __size, __bold, __italic)

        font = QFont(__family, __size, 1, __italic)
        font.setBold(__bold)

        return font