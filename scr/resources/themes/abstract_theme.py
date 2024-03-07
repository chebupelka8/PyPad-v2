from scr.scripts.tools.file import FileLoader


class AbstractTheme:
    theme = FileLoader.load_json(FileLoader.load_json("scr/data/settings.json")["theme"]["path"])

    @classmethod
    def reload_theme(cls) -> None:
        cls.theme = AbstractTheme.theme