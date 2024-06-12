from ...configs.patterns import JsonPatterns
from ..themes import JsonTheme
from .highlighter import CodeHighlighter


class JsonCodeHighLighter(CodeHighlighter):
    def __init__(self, target) -> None:
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(JsonPatterns.DIGITS, JsonTheme.DIGITS, text)
        self.highlight_match(JsonPatterns.BOOLEAN, JsonTheme.BOOLEAN, text)
        self.highlight_match(JsonPatterns.NULL_TYPE, JsonTheme.NULL_TYPE, text)
        self.highlight_match(JsonPatterns.SYMBOLS, JsonTheme.SYMBOLS, text)
        self.highlight_match(JsonPatterns.BRACKETS, JsonTheme.BRACKETS, text)
        self.highlight_match(JsonPatterns.STRING, JsonTheme.STRING, text)
