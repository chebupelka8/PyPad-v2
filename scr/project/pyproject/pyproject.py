from typing import Optional

import os
import json

from scr.scripts.tools.file import FileLoader
from .pyproject_config import PyProjectConfig


class PyProject:
    def __init__(self, __path: str) -> None:
        if self.__verify(__path):
            self.__path = __path

        else:
            print("Invalid project.")

    @staticmethod
    def __verify(__path: str) -> bool:
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
