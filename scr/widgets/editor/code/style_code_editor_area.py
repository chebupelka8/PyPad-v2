from scr.resources.highlighters import StyleCodeHighLighter
from scr.resources.themes import StyleTheme

from ..abstract.abstract_code_area import AbstractCodeEditorArea


class StyleCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str):
        super().__init__(__path, StyleCodeHighLighter, StyleTheme)

        # self.set_default_text_color(StyleTheme.DEFAULT)

    def keyPressEvent(self, event):
        self.key_press_filter(event, True, False, True, True, True)