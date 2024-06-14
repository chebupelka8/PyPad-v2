from scr.scripts.tools.chars import TextCharCreator

from .abstract_theme import AbstractTheme


class JsonTheme(AbstractTheme):
    theme = AbstractTheme.theme["json-theme"]

    DEFAULT = theme["default"]
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    BOOLEAN = TextCharCreator.create_char_format(*theme["boolean"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    NULL_TYPE = TextCharCreator.create_char_format(*theme["null-type"].values())
