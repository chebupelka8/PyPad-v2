import json

from ..file import FileLoader


class InterpreterManager:
    config = FileLoader.load_json("scr/data/conf.json")

    __python_interpreter_path = config["python_interpreter_path"]

    @staticmethod
    def __dump(__config) -> None:
        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(__config, file, indent=4)

    @classmethod
    def set_python_interpreter_path(cls, __path: str) -> None:
        cls.__python_interpreter_path = __path
        cls.config["python_interpreter_path"] = __path

        cls.__dump(cls.config)

    @classmethod
    def get_python_interpreter_path(cls) -> str:
        return cls.__python_interpreter_path

    @classmethod
    def remove_python_interpreter_path(cls) -> None:
        cls.__python_interpreter_path = ""
        cls.config["python_interpreter_path"] = ""

        cls.__dump(cls.config)
