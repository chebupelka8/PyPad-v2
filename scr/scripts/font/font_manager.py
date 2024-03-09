from ..tools.file import FileLoader
from .font import Font

from PySide6.QtGui import QFont

import json


class _FontManager:
    font_updaters = None
    directory = None

    @classmethod
    def get_current_font(cls) -> dict:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]

    @classmethod
    def get_current_font_as_font(cls) -> QFont:
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
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["family"]

    @classmethod
    def get_current_font_size(cls) -> int:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["size"]

    @classmethod
    def is_current_bold(cls) -> bool:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["bold"]

    @classmethod
    def is_current_italic(cls) -> bool:
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]["font"]["italic"]

    @classmethod
    def add_font_updater(cls, *__updaters):
        for i in __updaters: cls.font_updaters.append(i)

    @classmethod
    def set_current_font(
            cls,
            family: str | None = None,
            size: int | None = None,
            bold: bool | None = None,
            italic: bool | None = None
    ) -> None:
        data = FileLoader.load_json("scr/data/settings.json")

        if family is None: family = cls.get_current_family()
        if size is None: size = cls.get_current_font_size()
        if bold is None: bold = data[cls.directory]["font"]["bold"]
        if italic is None: italic = data[cls.directory]["font"]["italic"]

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
