from scr.scripts.tools.file import FileLoader


class VersionConfig:
    __config = FileLoader.load_json("scr/data/dist.json")

    name = __config["name"]
    version = __config["version"]
    build = __config["build"]
    author = __config["author"]
    author_social_link = __config["author-social-link"]
    project_page = __config["project-page"]
    license = __config["license"]

    @classmethod
    def welcome(cls) -> None:
        print("Welcome to PyPad!")
        print(cls.__repr__())

    @classmethod
    def __repr__(cls) -> str:
        return f"""\tVersion: {cls.version}\n\tBuild: {cls.build}\n\tAuthor: {cls.author}\n\tLicense: {cls.license}"""
