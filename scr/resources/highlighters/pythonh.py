from ...configs.patterns import PythonPatterns
from ..themes import PythonTheme
from .highlighter import CodeHighlighter


class PythonCodeHighlighter(CodeHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(PythonPatterns.CLASS_NAME, PythonTheme.CLASS_NAMES, text)
        self.highlight_match(PythonPatterns.FUNCTION_NAME, PythonTheme.FUNC_NAMES, text)
        self.highlight_match(PythonPatterns.KEYWORDS, PythonTheme.KEYWORDS, text)
        self.highlight_match(
            PythonPatterns.PYTHON_FUNCTIONS, PythonTheme.FUNCTIONS, text
        )
        self.highlight_match(PythonPatterns.BOOLEAN, PythonTheme.BOOLEAN, text)
        self.highlight_match(PythonPatterns.NONE_TYPE, PythonTheme.NONE_TYPE, text)
        self.highlight_match(PythonPatterns.DATA_TYPES, PythonTheme.DATA_TYPES, text)
        self.highlight_match(PythonPatterns.BRACKETS, PythonTheme.BRACKETS, text)
        self.highlight_match(PythonPatterns.SPECIAL, PythonTheme.SPECIAL, text)
        self.highlight_match(PythonPatterns.DIGITS, PythonTheme.DIGITS, text)
        self.highlight_match(PythonPatterns.PYTHON_SYMBOLS, PythonTheme.SYMBOLS, text)
        self.highlight_match(PythonPatterns.DECORATOR, PythonTheme.DECORATOR, text)
        self.highlight_match(PythonPatterns.COMMENT, PythonTheme.COMMENT, text)
        self.highlight_match(
            PythonPatterns.STRING_DOUBLE_QUOTATION, PythonTheme.STRING, text
        )
        self.highlight_match(PythonPatterns.STRING_APOSTROPHE, PythonTheme.STRING, text)
        self.highlight_match(PythonPatterns.LONG_STRING, PythonTheme.STRING, text)
