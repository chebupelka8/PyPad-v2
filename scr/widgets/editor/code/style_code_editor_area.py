from ..abstract.abstract_code_area import AbstractCodeEditorArea

from scr.resources.highlighters import StyleCodeHighLighter


class StyleCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str):
        super().__init__(__path)

        StyleCodeHighLighter(self)
        StyleCodeHighLighter(self.codeMap)
        # self.set_default_text_color(StyleTheme.DEFAULT)

    def keyPressEvent(self, event):
        self.key_press_filter(event, True, False, True, True, True)