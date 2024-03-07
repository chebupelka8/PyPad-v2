from ...tools.file import FileLoader

import json


class _SettingsUpdater:
    updaters = None
    directory = None

    @classmethod
    def get_settings(cls):
        return FileLoader.load_json("scr/data/settings.json")[cls.directory]

    @classmethod
    def call_updaters(cls):
        for upd in cls.updaters:
            upd()

    @classmethod
    def add_updater(cls, __command):
        cls.updaters.append(__command)


class EditorSettingsUpdater(_SettingsUpdater):
    updaters = []
    directory = "editor"

    @classmethod
    def set_cursor_style(cls, __style: str) -> None:
        settings = FileLoader.load_json("scr/data/settings.json")

        settings["editor"]["cursor"]["style"] = __style

        with open("scr/data/settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

        cls.call_updaters()

    @classmethod
    def set_tab_width(cls, __width: int) -> None:
        settings = FileLoader.load_json("scr/data/settings.json")

        settings["editor"]["tab-width"] = __width

        with open("scr/data/settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

        cls.call_updaters()

    @classmethod
    def get_cursor_style(cls) -> str:
        return cls.get_settings()["cursor"]["style"]

    @classmethod
    def get_tab_width(cls) -> int:
        return cls.get_settings()["tab-width"]


class WorkbenchSettingsUpdater(_SettingsUpdater):
    updaters = []
    directory = "workbench"
