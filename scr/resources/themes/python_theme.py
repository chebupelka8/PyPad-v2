from scr.scripts.tools.chars import TextCharCreator

from .abstract_theme import AbstractTheme


class PythonTheme(AbstractTheme):
    theme = AbstractTheme.theme["python-theme"]

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
