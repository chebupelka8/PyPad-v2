from ...scripts.tools.chars import TextCharCreator
from ...scripts.tools.file import FileLoader


class _AbstractTheme:
    theme = FileLoader.load_json(FileLoader.load_json("scr/data/settings.json")["theme"]["path"])

    @classmethod
    def reload_theme(cls) -> None:
        cls.theme = _AbstractTheme.theme


class TextEditorTheme(_AbstractTheme):
    theme = _AbstractTheme.theme["text-editor-theme"]

    DEFAULT = theme["default"]


class PythonTheme(_AbstractTheme):
    theme = _AbstractTheme.theme["python-theme"]

    DEFAULT = theme["default"]
    KEYWORDS = TextCharCreator.create_char_format(*theme["keywords"].values())
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    COMMENT = TextCharCreator.create_char_format(*theme["comment"].values())
    DECORATOR = TextCharCreator.create_char_format(*theme["decorator"].values())
    CLASS_NAMES = TextCharCreator.create_char_format(*theme["class-names"].values())
    FUNC_NAMES = TextCharCreator.create_char_format(*theme["func-names"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    BOOLEAN = TextCharCreator.create_char_format(*theme["boolean"].values())
    NONE_TYPE = TextCharCreator.create_char_format(*theme["none-type"].values())
    DATA_TYPES = TextCharCreator.create_char_format(*theme["data-types"].values())
    FUNCTIONS = TextCharCreator.create_char_format(*theme["functions"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    SPECIAL = TextCharCreator.create_char_format(*theme["special"].values())


class JsonTheme(_AbstractTheme):
    theme = _AbstractTheme.theme["json-theme"]

    DEFAULT = theme["default"]
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    BOOLEAN = TextCharCreator.create_char_format(*theme["boolean"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    NULL_TYPE = TextCharCreator.create_char_format(*theme["null-type"].values())


class StyleTheme(_AbstractTheme):
    theme = _AbstractTheme.theme["style-theme"]

    DEFAULT = theme["default"]
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    COMMENT = TextCharCreator.create_char_format(*theme["comment"].values())


class HtmlTheme(_AbstractTheme):
    theme = _AbstractTheme.theme["html-theme"]

    DEFAULT = theme["default"]
    TAGS = TextCharCreator.create_char_format(*theme["tags"].values())
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    COMMENT = TextCharCreator.create_char_format(*theme["comment"].values())
