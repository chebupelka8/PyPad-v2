import json
import os

from ..tools.file import FileLoader


class ThemeManager:
    theme = FileLoader.load_json("scr/data/settings.json")["theme"]
    unsaved: dict | None = None

    @classmethod
    def get_current_theme_path(cls) -> str:
        """
        Get the path of the current theme.

        Returns:
        str: The path of the current theme.
        """

        return cls.theme["path"]

    @classmethod
    def get_current_theme_name(cls) -> str:
        """
        Get the name of the current theme.

        Returns:
        str: The name of the current theme.
        """

        return cls.theme["name"]

    @classmethod
    def set_current_theme_by_path(cls, __path: str) -> None:
        """
        Set the current theme by specifying its path.

        Parameters:
        __path (str): The path of the new theme.
        """

        settings = FileLoader.load_json("scr/data/settings.json")
        settings["theme"] = {
            "path": __path,
            "name": FileLoader.load_json(__path)["name"],
        }

        cls.unsaved = settings

    @classmethod
    def set_current_theme_by_name(cls, __name: str) -> None:
        """
        Set the current theme by specifying its name.

        Parameters:
        __name (str): The name of the new theme.
        """

        settings = FileLoader.load_json("scr/data/settings.json")
        settings["theme"] = {"path": cls.get_theme_path_by_name(__name), "name": __name}

        cls.unsaved = settings

    @classmethod
    def save(cls) -> None:
        """
        Save the changes made to the theme settings.
        """

        if cls.unsaved is not None:
            with open("scr/data/settings.json", "w", encoding="utf-8") as file:
                json.dump(cls.unsaved, file, indent=4)

        cls.theme = FileLoader.load_json("scr/data/settings.json")["theme"]
        cls.unsaved = None

    @staticmethod
    def get_theme_path_by_name(__name: str) -> str:
        """
        Get the path of a theme by its name.

        Parameters:
        __name (str): The name of the theme.

        Returns:
        str: The path of the theme with the specified name.
        """

        themes = {
            FileLoader.load_json(f"scr/data/themes/{i}")["name"]: f"scr/data/themes/{i}"
            for i in os.listdir("scr/data/themes")
        }

        for name in themes.keys():
            if name == __name:
                return themes[__name]
