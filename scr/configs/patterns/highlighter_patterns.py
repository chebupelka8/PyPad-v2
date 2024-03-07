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
    COMMENT = r'#[^\n]*' # ^(?!").*$  |  ^(?!").*$  |  (?!")^#[^\n]*

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