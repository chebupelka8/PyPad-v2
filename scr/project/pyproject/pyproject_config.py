import json
import os

from scr.scripts.tools.file import FileLoader
from scr.project import ImageGenerator, ProjectNameGenerator


class PyProjectConfig:
    config = FileLoader.load_json("scr/data/conf.json")

    __directory = config["directory"]
    __projects = config["pyprojects"]

    @staticmethod
    def __dump(__config) -> None:
        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(__config, file, indent=4)

    @classmethod
    def __update(cls) -> None:
        config = FileLoader.load_json("scr/data/conf.json")

        cls.__directory = config["directory"]
        cls.__projects = config["pyprojects"]

    @classmethod
    def get_projects(cls) -> list[dict]:
        return cls.__projects

    @classmethod
    def get_projects_names(cls) -> list[str]:
        return list(cls.__projects.keys())

    @classmethod
    def get_project_icons(cls) -> list[str]:
        return [cls.__projects[i]["icon"] for i in cls.__projects]

    @classmethod
    def get_info_projects(cls) -> dict:
        res = {}

        for project in cls.__projects:
            res[os.path.basename(project)] = project

        return res

    @classmethod
    def add_project(cls, __path, __name) -> None:
        config = FileLoader.load_json("scr/data/conf.json")
        config["pyprojects"][__name] = {
            "path": __path,
            "icon": ImageGenerator.save(
                __name,
                ImageGenerator.generate((300, 300), ProjectNameGenerator.get_basename(__name))
            )
        }

        cls.__dump(config)
        cls.__update()
