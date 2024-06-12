from scr.scripts.tools.chars import TextCharCreator

from .abstract_theme import AbstractTheme


class StyleTheme(AbstractTheme):
    theme = AbstractTheme.theme["style-theme"]

    DEFAULT = theme["default"]
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    DIGITS = TextCharCreator.create_char_format(*theme["digits"].values())
    BRACKETS = TextCharCreator.create_char_format(*theme["brackets"].values())
    COMMENT = TextCharCreator.create_char_format(*theme["comment"].values())

