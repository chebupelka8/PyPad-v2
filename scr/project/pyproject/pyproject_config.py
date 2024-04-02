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
        """
        Dumps the configuration to the JSON file.

        Parameters:
        __config: The configuration to be dumped.
        """

        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(__config, file, indent=4)

    @classmethod
    def __update(cls) -> None:
        """
        Updates the class attributes with the latest configuration data.
        """

        config = FileLoader.load_json("scr/data/conf.json")

        cls.__directory = config["directory"]
        cls.__projects = config["pyprojects"]

    @classmethod
    def get_projects(cls) -> list[dict]:
        """
        Retrieves a list of all projects with their details.

        Returns:
        list[dict]: List of projects with their details.
        """

        return cls.__projects

    @classmethod
    def get_projects_names(cls) -> list[str]:
        """
        Retrieves a list of project names.

        Returns:
        list[str]: List of project names.
        """

        return list(cls.__projects.keys())

    @classmethod
    def get_project_icons(cls) -> list[str]:
        """
        Retrieves a list of project icons.

        Returns:
        list[str]: List of project icons.
        """

        return [cls.__projects[i]["icon"] for i in cls.__projects]

    @classmethod
    def get_info_projects(cls) -> dict:
        """
        Retrieves a dictionary of project names and paths.

        Returns:
        dict: Dictionary of project names and paths.
        """

        res = {}

        for project in cls.__projects:
            res[os.path.basename(project)] = project

        return res

    @classmethod
    def add_project(cls, __path: str, __name: str) -> None:
        """
        Adds a new project to the configuration.

        Parameters:
        __path (str): The path of the new project.
        __name (str): The name of the new project.
        """

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

    @classmethod
    def remove_project(cls, __name: str) -> None:
        """
        Removes a project from the configuration.

        Parameters:
        __name (str): The name of the project to be removed.
        """

        config = FileLoader.load_json("scr/data/conf")
        del config["pyprojects"][__name]

        cls.__dump(config)
        cls.__update()
