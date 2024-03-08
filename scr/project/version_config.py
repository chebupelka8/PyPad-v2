from scr.scripts.tools.file import FileLoader


class VersionConfig:
    __config = FileLoader.load_json("scr/data/dist.json")

    name = __config["name"]
    version = __config["version"]
    build = __config["build"]
