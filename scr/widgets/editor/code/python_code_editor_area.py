from ..abstract.abstract_code_area import AbstractCodeEditorArea

from PySide6.QtCore import Qt

from scr.resources.highlighters import PythonCodeHighlighter
from scr.resources.themes import PythonTheme
from scr.scripts.tools.code import CodeAnalyzer


class PythonCodeEditorArea(AbstractCodeEditorArea):
    def __init__(self, __path: str):
        super().__init__(__path, PythonCodeHighlighter, PythonTheme)

        # self.set_default_text_color(PythonTheme.DEFAULT)

    def keyPressEvent(self, event):
        key_func = lambda: (
            self.key_press_filter(event, True, True, True, True, True)
        )

        self.lineNumberArea.update()

        if event.key() == Qt.Key.Key_Return:
            cursor = self.textCursor()
            previous = self.get_current_line_text()

            if previous == "":
                prev = "//"  # it's need for remove exception - list has no index -1

            elif not previous.isspace() and previous.strip(" ") != "":
                try:
                    prev = previous[:cursor.positionInBlock()].rstrip()
                    prev[-1]  # checks if there is a character at the end of the line

                except IndexError:
                    prev = "//"
            else:
                prev = previous

            if prev[-1] == ":" or self.get_current_line_text()[:1] == "\t" or self.get_current_line_text()[:4] == "    ":
                tab_count = (
                    CodeAnalyzer.find_tabs_in_string(previous, cursor.positionInBlock()) +
                    CodeAnalyzer.check_last_character_is_colon(prev) +
                    CodeAnalyzer.find_tabs_in_string_by_spaces(
                        previous, cursor.positionInBlock(), self.get_current_tab_width()
                    )
                )
                cursor.insertText("\n" + ("\t" * tab_count))

            else:
                key_func()

        else:
            key_func()
