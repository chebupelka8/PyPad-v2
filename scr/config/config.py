from PySide6.QtGui import QTextCharFormat, QFont, QColor

from scr.scripts import FileLoader

import scr.config.ico_cfg


WINDOW_SIZE = (1200, 800)


class IconPaths:

    class FileIcons:
        PYTHON = ":/file_icons/python.png"
        CSS = ":/file_icons/css.png"
        JSON = ":/file_icons/json.png"
        TXT = ":/file_icons/txt.png"
        PICTURE = ":/file_icons/image.png"
        HTML = ":/file_icons/html.png"
        JS = ":/file_icons/js.png"
        JAVA = ":/file_icons/java.png"
        README = ":/file_icons/readme.png"
        ZIP = ":/zip-file.png"
        DEFAULT = ":/symbol.png"

    class SystemIcons:
        MAIN = ":/system_icons/window_icon.png"
        WELCOME = ":/system_icons/welcome.png"
        APPS = ":/system_icons/apps.png"
        FOLDER_OPEN = ":/system_icons/folder-open.png"
        SEARCH = ":/system_icons/search.png"
        RUN = ":/system_icons/play.png"
        SETTINGS = ":/system_icons/settings.png"
        LOGO = ":/system_icons/Logo PyPad.png"

    class FolderIcons:
        DEFAULT = ":/folder_icons/Yellow-folder.ico"
        MUSIC = ":/folder_icons/Yellow-folder-music.ico"
        PICTURE = ":/folder_icons/Yellow-folder-pictures.ico"


class PythonPatterns:
    KEYWORDS = r"""\b(and|as|assert|async|await|break|class|continue
    |def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal
    |not|or|pass|raise|return|try|while|with|yield|case|match)\b"""

    CLASS_NAME = r'\bclass\b\s*(\w+)'

    FUNCTION_NAME = r'\bdef\b\s*(\w+)'

    PYTHON_FUNCTIONS = r"""\b(divmod|map|filter|zip|super|open|help|hex|abs|eval|exec|ord|chr|sorted
    |reversed|enumerate|range|sum|repr|round|type|all|any|print|input|len|max|min|hash|dir|bytearray
    |bytes|callable|hasattr|delattr|format|frozenset|getattr|id|issubclass|isinstance|locals|memoryview
    |next|oct|pow|property|repr|staticmethod|vars|setattr|slice|compile|complex|classmethod|globals)\b"""

    BOOLEAN = r"\b(True|False)\b"
    NONE_TYPE = r"\b(None)\b"
    DATA_TYPES = r"\b(int|float|str|dict|set|tuple|list|bool|iter|object)\b"

    SPECIAL = r"\b(self|cls)\b"

    BRACKETS = r"\(|\)|\[|\]|\{|\}"
    DIGITS = r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b'
    PYTHON_SYMBOLS = r"\=|\+|\-|\>|\&|\<|\%|\/|\*|\|"

    DECORATOR = r'@[^\n]*'
    COMMENT = r'#[^\n]* $' # ^(?!").*$  |  ^(?!").*$  |  (?!")^#[^\n]*

    STRING_DOUBLE_QUOTATION = r'"[^"\\]*(\\.[^"\\]*)*"'
    STRING_APOSTROPHE = r"'[^'\\]*(\\.[^'\\]*)*'"
    LONG_STRING = r'""".*?"""|""".*?'


class JsonPatterns:
    STRING = r'".*?\n*?"|".*?'
    BRACKETS = r"\[|\]|\{|\}"
    BOOLEAN = r"\b(true|false)\b"
    SYMBOLS = r"\,\:"
    DIGITS = r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b'
    NULL_TYPE = r"\bnull\b"


class StylePatterns:
    BRACKETS = r"\[|\]|\{|\}|\(|\)"
    SYMBOLS = r"\,\:"
    DIGITS = r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b'
    COMMENT = r'\/*[^"\\]*(\\.[^"\\]*)*\*\/'


class HtmlPatterns:
    TAGS = r"<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
    STRING = r'"[^"\\]*(\\.[^"\\]*)*"'
    SYMBOLS = r"\<\>\/"
    COMMENT = r"\<\!\-\-[^'\\]*(\\.[^'\\]*)*\-\-\>"


class TextCharCreator:

    @staticmethod
    def create_char_format(__color: str, italic: bool = False, bold: bool = False) -> QTextCharFormat:
        res = QTextCharFormat()
        res.setForeground(QColor(__color))
        res.setFontItalic(italic)
        if bold:
            res.setFontWeight(QFont.Bold)

        return res

    @classmethod
    def create_char_format_background(cls, __bg_color: str, italic: bool = False, bold: bool = False):
        res = QTextCharFormat()
        res.setForeground(QColor(__bg_color))
        res.setFontItalic(italic)
        if bold:
            res.setFontWeight(QFont.Bold)

        return res


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
