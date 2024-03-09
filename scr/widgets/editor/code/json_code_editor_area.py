from ..abstract.abstract_code_area import AbstractCodeEditorArea

from scr.resources.highlighters import JsonCodeHighLighter
from scr.resources.themes import JsonTheme


class JsonCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str):
        super().__init__(__path, JsonCodeHighLighter, JsonTheme)

        # self.set_default_text_color(JsonTheme.DEFAULT)

    def keyPressEvent(self, event):
        self.key_press_filter(event, False, True, True, True, False)
