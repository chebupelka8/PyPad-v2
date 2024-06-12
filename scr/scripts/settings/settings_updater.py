import json

from scr.scripts.tools.file import FileLoader


class _SettingsUpdater:
    updaters = None
    directory = None

    @classmethod
    def get_settings(cls):
        """
        Get the settings from the specified directory.

        Returns:
        dict: The settings from the specified directory.
        """

        return FileLoader.load_json("scr/data/settings.json")[cls.directory]

    @classmethod
    def call_updaters(cls):
        """
        Call all the registered updaters.
        """

        for upd in cls.updaters:
            upd()

    @classmethod
    def add_updater(cls, __command):
        """
        Add an updater command to the list of updaters.

        Args:
        __command: The updater command to add.
        """

        cls.updaters.append(__command)


class EditorSettingsUpdater(_SettingsUpdater):
    updaters = []
    directory = "editor"

    @classmethod
    def set_cursor_style(cls, __style: str) -> None:
        """
        Set the cursor style in the editor settings.

        Args:
        __style (str): The cursor style to set.
        """

        settings = FileLoader.load_json("scr/data/settings.json")

        settings["editor"]["cursor"]["style"] = __style

        with open("scr/data/settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

        cls.call_updaters()

    @classmethod
    def set_tab_width(cls, __width: int) -> None:
        """
        Set the tab width in the editor settings.

        Args:
        __width (int): The tab width to set.
        """

        settings = FileLoader.load_json("scr/data/settings.json")

        settings["editor"]["tab-width"] = __width

        with open("scr/data/settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

        cls.call_updaters()

    @classmethod
    def get_cursor_style(cls) -> str:
        """
        Get the cursor style from the editor settings.

        Returns:
        str: The cursor style.
        """

        return cls.get_settings()["cursor"]["style"]

    @classmethod
    def get_tab_width(cls) -> int:
        """
        Get the tab width from the editor settings.

        Returns:
        int: The tab width.
        """

        return cls.get_settings()["tab-width"]


class WorkbenchSettingsUpdater(_SettingsUpdater):
    updaters = []
    directory = "workbench"
