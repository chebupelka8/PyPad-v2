import json

from scr.scripts.tools.file import FileLoader


class ProjectConfig:
    config = FileLoader.load_json("scr/data/conf.json")

    __directory = config["directory"]

    @staticmethod
    def __dump(__config) -> None:
        """
        Dump the given configuration to the 'conf.json' file.

        Args:
            __config: The configuration to dump.
        """

        with open("scr/data/conf.json", "w", encoding="utf-8") as file:
            json.dump(__config, file, indent=4)

    @classmethod
    def set_directory(cls, __dir: str) -> None:
        """
        Set the project directory in the configuration.

        Args:
            __dir (str): The directory to set.
        """

        cls.__directory = __dir

        config = FileLoader.load_json("scr/data/conf.json")
        config["directory"] = __dir

        cls.__dump(config)

    @classmethod
    def get_directory(cls) -> str:
        """
        Get the current project directory from the configuration.

        Returns:
            str: The current project directory.
        """

        return cls.__directory