from typing import Optional

import os
import json

from scr.scripts.tools.file import FileLoader
from .pyproject_config import PyProjectConfig


class PyProject:
    def __init__(self, __path: str) -> None:
        """
        Initializes a PyProject instance.

        Parameters:
        __path (str): The path to the project.

        Notes:
        - Verifies the project path and sets it if valid.
        - Prints "Invalid project" if verification fails.
        """

        if self.__verify(__path):
            self.__path = __path

        else:
            print("Invalid project.")

    @staticmethod
    def __verify(__path: str) -> bool:
        """
        Verifies the existence of a PyPad project.

        Parameters:
        __path (str): The path to check for the project.

        Returns:
        bool: True if the project is valid, False otherwise.
        """

        return ".pypad" in os.listdir(__path) and os.path.exists(os.path.join(__path, ".pypad\\config.json"))


class SetupPyProject:
    WELCOME_SCRIPT = """
def main() -> None:
    # Welcome to PyPad!
    print('Hello world!')


if __name__ == '__main__':
    main()
    """

    config = FileLoader.load_json("scr/data/conf.json")
    __python_interpreter_path = config["python_interpreter_path"]

    @classmethod
    def create_new_project(cls, __path: str, __name: str, __version: Optional[str] = None,
                           make_welcome_script: bool = True, after_command = None) -> None:
        """
        Creates a new PyPad project.

        Parameters:
        __path (str): The path where the project will be created.
        __name (str): The name of the project.
        __version (Optional[str]): The version of the project.
        make_welcome_script (bool): Flag to include a welcome script.
        after_command: Optional callback function to execute after project creation.

        Notes:
        - Checks if the project name already exists.
        - Executes batch scripts to set up the project and virtual environment.
        - Saves project data to a config file.
        - Creates a welcome script if specified.
        - Adds the project to PyProjectConfig.
        - Executes the after_command if provided.
        """

        if __name in PyProjectConfig.get_projects_names():
            return

        output_path = os.path.join(__path, __name)

        os.system(f'call scr\\project\\pyproject\\scripts\\create_pyproject.bat "{__path}" "{__name}"')
        os.system(f'call scr\\project\\pyproject\\scripts\\virtual_venv.bat "{output_path}" "{cls.__python_interpreter_path}"')

        data = {
            "name": __name,
            "version": __version
        }

        with open(f'{__path}\\{__name}\\.pypad\\config.json', "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        # create a welcome script
        with open(f'{__path}\\{__name}\\main.py', "w", encoding="utf-8") as file:
            if make_welcome_script:
                file.write(cls.WELCOME_SCRIPT)
            else:
                file.write("")

        PyProjectConfig.add_project(output_path, os.path.basename(output_path))
        if after_command is not None: after_command()
