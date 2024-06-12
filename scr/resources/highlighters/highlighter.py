import re

from PySide6.QtGui import QSyntaxHighlighter


class CodeHighlighter(QSyntaxHighlighter):
    def __init__(self, target):
        super().__init__(target)

    def highlight_match(self, __pattern, __format, __text):
        for match in re.finditer(__pattern, __text):
            start = match.start()
            count = match.end() - match.start()

            self.setFormat(start, count, __format)
