from .abstract_theme import AbstractTheme

from scr.scripts.tools.chars import TextCharCreator


class HtmlTheme(AbstractTheme):
    theme = AbstractTheme.theme["html-theme"]

    DEFAULT = theme["default"]
    TAGS = TextCharCreator.create_char_format(*theme["tags"].values())
    STRING = TextCharCreator.create_char_format(*theme["string"].values())
    SYMBOLS = TextCharCreator.create_char_format(*theme["symbols"].values())
    COMMENT = TextCharCreator.create_char_format(*theme["comment"].values())
