from ..abstract.abstract_code_area import AbstractCodeEditorArea

from scr.resources.highlighters import HtmlCodeHighlighter


class HtmlCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str | None = None):
        super().__init__(__path)

        HtmlCodeHighlighter(self)
        HtmlCodeHighlighter(self.codeMap)
        # self.set_default_text_color(HtmlTheme.DEFAULT)

    def keyPressEvent(self, event):
        self.key_press_filter(
            event, False, False, False, True, True, True
        )
