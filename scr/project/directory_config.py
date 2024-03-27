import json

from scr.scripts.tools.file import FileLoader


class ProjectConfig:
    config = FileLoader.load_json("scr/data/conf.json")

    __directory = config["directory"]

    @staticmethod
    def __dump(__config) -> None:
        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(__config, file, indent=4)

    @classmethod
    def set_directory(cls, __dir: str) -> None:
        cls.__directory = __dir

        config = FileLoader.load_json("scr/data/conf.json")
        config["directory"] = __dir

        cls.__dump(config)

    @classmethod
    def get_directory(cls) -> str:
        return cls.__directory