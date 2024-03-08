import json

from scr.scripts.tools.file import FileLoader


class ProjectConfig:
    config = FileLoader.load_json("scr/data/conf.json")

    __directory = config["directory"]

    @classmethod
    def set_directory(cls, __dir: str) -> None:
        cls.__directory = __dir

        config = FileLoader.load_json("scr/data/conf.json")
        config["directory"] = __dir

        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)

    @classmethod
    def get_directory(cls) -> str:
        return cls.__directory