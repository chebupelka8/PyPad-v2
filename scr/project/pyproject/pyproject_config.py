import json

from scr.scripts.tools.file import FileLoader


class PyProjectConfig:
    config = FileLoader.load_json("scr/data/conf.json")

    __directory = config["directory"]
    __projects = config["pyprojects"]

    @staticmethod
    def __dump(__config) -> None:
        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(__config, file, indent=4)

    @classmethod
    def __get_project_by_name(cls, name: str):
        ...

    @classmethod
    def get_projects(cls) -> list[dict]:
        return cls.__projects

    @classmethod
    def add_project(cls, __path, __name) -> None:
        config = FileLoader.load_json("scr/data/conf.json")
        config["projects"][__name] = __path

        cls.__dump(config)