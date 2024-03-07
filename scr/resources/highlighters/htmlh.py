from .highlighter import CodeHighlighter
from ...configs.patterns import HtmlPatterns
from ..themes import HtmlTheme


class HtmlCodeHighlighter(CodeHighlighter):
    def __init__(self, target):
        super().__init__(target.document())

    def highlightBlock(self, text):
        self.highlight_match(HtmlPatterns.TAGS, HtmlTheme.TAGS, text)
        self.highlight_match(HtmlPatterns.STRING, HtmlTheme.STRING, text)
        self.highlight_match(HtmlPatterns.SYMBOLS, HtmlTheme.SYMBOLS, text)
        self.highlight_match(HtmlPatterns.COMMENT, HtmlTheme.COMMENT, text)
