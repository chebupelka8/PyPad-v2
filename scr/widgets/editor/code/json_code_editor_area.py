from ..abstract.abstract_code_area import AbstractCodeEditorArea

from scr.resources.highlighters import JsonCodeHighLighter


class JsonCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__(__path)

        JsonCodeHighLighter(self)
        JsonCodeHighLighter(self.codeMap)
        # self.set_default_text_color(JsonTheme.DEFAULT)

    def keyPressEvent(self, event):
        self.key_press_filter(event, False, True, True, True, False)
