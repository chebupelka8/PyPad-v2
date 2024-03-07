from .highlighter import CodeHighlighter
from ...configs.patterns import StylePatterns
from ..themes import StyleTheme


class StyleCodeHighLighter(CodeHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(StylePatterns.DIGITS, StyleTheme.DIGITS, text)
        self.highlight_match(StylePatterns.BRACKETS, StyleTheme.BRACKETS, text)
        self.highlight_match(StylePatterns.SYMBOLS, StyleTheme.SYMBOLS, text)
        self.highlight_match(StylePatterns.COMMENT, StyleTheme.COMMENT, text)
