from scr.config import (
    PythonPatterns, PythonTheme, JsonPatterns,
    JsonTheme, StylePatterns, StyleTheme,
    HtmlPatterns, HtmlTheme, TextCharCreator
)

from PySide6.QtGui import QSyntaxHighlighter

import re


class _CodeHighlighter(QSyntaxHighlighter):
    def __init__(self, target):
        super().__init__(target)

    def highlight_match(self, __pattern, __format, __text):
        for match in re.finditer(__pattern, __text):
            start = match.start()
            count = match.end() - match.start()

            self.setFormat(start, count, __format)


class PythonCodeHighlighter(_CodeHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(PythonPatterns.CLASS_NAME, PythonTheme.CLASS_NAMES, text)
        self.highlight_match(PythonPatterns.FUNCTION_NAME, PythonTheme.FUNC_NAMES, text)
        self.highlight_match(PythonPatterns.KEYWORDS, PythonTheme.KEYWORDS, text)
        self.highlight_match(PythonPatterns.PYTHON_FUNCTIONS, PythonTheme.FUNCTIONS, text)
        self.highlight_match(PythonPatterns.BOOLEAN, PythonTheme.BOOLEAN, text)
        self.highlight_match(PythonPatterns.NONE_TYPE, PythonTheme.NONE_TYPE, text)
        self.highlight_match(PythonPatterns.DATA_TYPES, PythonTheme.DATA_TYPES, text)
        self.highlight_match(PythonPatterns.BRACKETS, PythonTheme.BRACKETS, text)
        self.highlight_match(PythonPatterns.SPECIAL, PythonTheme.SPECIAL, text)
        self.highlight_match(PythonPatterns.DIGITS, PythonTheme.DIGITS, text)
        self.highlight_match(PythonPatterns.PYTHON_SYMBOLS, PythonTheme.SYMBOLS, text)
        self.highlight_match(PythonPatterns.DECORATOR, PythonTheme.DECORATOR, text)
        self.highlight_match(PythonPatterns.COMMENT, PythonTheme.COMMENT, text)
        self.highlight_match(PythonPatterns.STRING_DOUBLE_QUOTATION, PythonTheme.STRING, text)
        self.highlight_match(PythonPatterns.STRING_APOSTROPHE, PythonTheme.STRING, text)
        self.highlight_match(PythonPatterns.LONG_STRING, PythonTheme.STRING, text)


class JsonCodeHighLighter(_CodeHighlighter):
    def __init__(self, target) -> None:
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(JsonPatterns.DIGITS, JsonTheme.DIGITS, text)
        self.highlight_match(JsonPatterns.BOOLEAN, JsonTheme.BOOLEAN, text)
        self.highlight_match(JsonPatterns.NULL_TYPE, JsonTheme.NULL_TYPE, text)
        self.highlight_match(JsonPatterns.SYMBOLS, JsonTheme.SYMBOLS, text)
        self.highlight_match(JsonPatterns.BRACKETS, JsonTheme.BRACKETS, text)
        self.highlight_match(JsonPatterns.STRING, JsonTheme.STRING, text)


class StyleCodeHighLighter(_CodeHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(StylePatterns.DIGITS, StyleTheme.DIGITS, text)
        self.highlight_match(StylePatterns.BRACKETS, StyleTheme.BRACKETS, text)
        self.highlight_match(StylePatterns.SYMBOLS, StyleTheme.SYMBOLS, text)
        self.highlight_match(StylePatterns.COMMENT, StyleTheme.COMMENT, text)


class HtmlCodeHighlighter(_CodeHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(HtmlPatterns.TAGS, HtmlTheme.TAGS, text)
        self.highlight_match(HtmlPatterns.STRING, HtmlTheme.STRING, text)
        self.highlight_match(HtmlPatterns.SYMBOLS, HtmlTheme.SYMBOLS, text)
        self.highlight_match(HtmlPatterns.COMMENT, HtmlTheme.COMMENT, text)
