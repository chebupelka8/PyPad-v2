import json

from ..file.file_loader import FileLoader

import os


class ThemeManager:
    theme = FileLoader.load_json("scr/data/settings.json")["theme"]
    unsaved: dict | None = None

    @classmethod
    def get_current_theme_path(cls) -> str:
        return cls.theme["path"]

    @classmethod
    def get_current_theme_name(cls) -> str:
        return cls.theme["name"]

    @classmethod
    def set_current_theme_by_path(cls, __path: str) -> None:
        settings = FileLoader.load_json("scr/data/settings.json")
        settings["theme"] = {
            "path": __path,
            "name": FileLoader.load_json(__path)["name"]
        }

        cls.unsaved = settings

    @classmethod
    def set_current_theme_by_name(cls, __name: str) -> None:
        settings = FileLoader.load_json("scr/data/settings.json")
        settings["theme"] = {
            "path": cls.get_theme_path_by_name(__name),
            "name": __name
        }

        cls.unsaved = settings

    @classmethod
    def save(cls) -> None:
        if cls.unsaved is not None:
            with open("scr/data/settings.json", "w", encoding="utf-8") as file:
                json.dump(cls.unsaved, file, indent=4)

        cls.theme = FileLoader.load_json("scr/data/settings.json")["theme"]
        cls.unsaved = None

    @staticmethod
    def get_theme_path_by_name(__name: str) -> str:
        themes = {
            FileLoader.load_json(f"scr/data/themes/{i}")["name"]: f"scr/data/themes/{i}"
            for i in os.listdir("scr/data/themes")
        }

        for name in themes.keys():
            if name == __name:
                return themes[__name]
