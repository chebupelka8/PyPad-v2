import json

from PySide6.QtGui import QFont

from ..tools.file import FileLoader
from .font import Font


class _FontManager:
    font_updaters = None
    directory = None

    @classmethod
    def get_current_font(cls) -> dict:
        """
        Get the current font settings from the settings file for the specified directory.

        Returns:
            dict: Current font settings.
        """

        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]

    @classmethod
    def get_current_font_as_font(cls) -> QFont:
        """
        Get the current font as a QFont object.

        Returns:
            QFont: Current font as a QFont object.
        """

        current_font = cls.get_current_font()

        if current_font["family"] not in Font.get_all_font_families():
            try:
                return Font.get_font_by_path(*current_font.values())

            except IndexError:
                return Font.get_system_font(*current_font.values())

        else:
            return Font.get_system_font(*current_font.values())

    @classmethod
    def get_current_family(cls) -> str:
        """
        Get the current font family.

        Returns:
            str: Current font family.
        """

        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"][
            "family"
        ]

    @classmethod
    def get_current_font_size(cls) -> int:
        """
        Get the current font size.

        Returns:
            int: Current font size.
        """

        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"][
            "size"
        ]

    @classmethod
    def is_current_bold(cls) -> bool:
        """
        Check if the current font is bold.

        Returns:
            bool: True if the current font is bold, False otherwise.
        """

        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"][
            "bold"
        ]

    @classmethod
    def is_current_italic(cls) -> bool:
        """
        Check if the current font is italic.

        Returns:
            bool: True if the current font is italic, False otherwise.
        """

        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"][
            "italic"
        ]

    @classmethod
    def add_font_updater(cls, *__updaters):
        """
        Add font updaters to the font manager.

        Args:
            *__updaters: Variable number of font updaters to add.
        """

        for i in __updaters:
            cls.font_updaters.append(i)

    @classmethod
    def set_current_font(
        cls,
        family: str | None = None,
        size: int | None = None,
        bold: bool | None = None,
        italic: bool | None = None,
    ) -> None:
        """
        Set the current font settings and update the settings file.

        Args:
            family (str | None): Font family to set. Defaults to None.
            size (int | None): Font size to set. Defaults to None.
            bold (bool | None): Bold setting to set. Defaults to None.
            italic (bool | None): Italic setting to set. Defaults to None.
        """

        data = FileLoader.load_json("scr/data/settings.json")

        if family is None:
            family = cls.get_current_family()
        if size is None:
            size = cls.get_current_font_size()
        if bold is None:
            bold = data[cls.directory]["font"]["bold"]
        if italic is None:
            italic = data[cls.directory]["font"]["italic"]

        data[cls.directory]["font"] = {
            "family": family,
            "size": size,
            "bold": bold,
            "italic": italic,
        }

        with open("scr/data/settings.json", "w") as file:
            json.dump(data, file, indent=4)

        for updater in cls.font_updaters:
            updater()


class EditorFontManager(_FontManager):
    font_updaters = []
    directory = "editor"


class WorkbenchFontManager(_FontManager):
    font_updaters = []
    directory = "workbench"
