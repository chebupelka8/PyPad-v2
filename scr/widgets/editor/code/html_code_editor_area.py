from ..abstract.abstract_code_area import AbstractCodeEditorArea

from scr.resources.highlighters import HtmlCodeHighlighter
from scr.resources.themes import HtmlTheme


class HtmlCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str):
        super().__init__(__path, HtmlCodeHighlighter, HtmlTheme)

        # self.set_default_text_color(HtmlTheme.DEFAULT)

    def keyPressEvent(self, event):
        self.key_press_filter(
            event, False, False, False, True, True, True
        )
