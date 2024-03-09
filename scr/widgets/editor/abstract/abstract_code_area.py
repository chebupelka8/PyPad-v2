from .abstract_text_area import TextEditorArea

from scr.scripts.tools.file import FileLoader
from scr.scripts.tools.code import CodeAnalyzer

from scr.widgets import CodeGlanceMap

from PySide6.QtCore import Qt


class AbstractCodeEditorArea(TextEditorArea):
    def __init__(self, __path: str, highlighter=None, theme=None):
        super().__init__()

        # insert text
        text = FileLoader.load_text(__path)
        text = CodeAnalyzer.refactor_spaces_to_tabs(text, CodeAnalyzer.get_tab_width_by_text(text))
        self.insertPlainText(text)

        # glance setup
        self.codeMap = CodeGlanceMap(text, self.font())

        # theme
        if theme is not None:
            self.set_default_text_color(theme.DEFAULT)
            self.codeMap.set_default_text_color(theme.DEFAULT)

        # highlighter
        if highlighter is not None:
            highlighter(self)
            highlighter(self.codeMap)

        # connections
        self.textChanged.connect(lambda: self.codeMap.setPlainText(self.toPlainText()))
        self.mainLayout.addWidget(self.codeMap, alignment=Qt.AlignmentFlag.AlignRight)

        # setup style sheet
        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/editor_area.css"))
        self.setObjectName("code-area")

        self.__path = __path

    def get_full_path(self):
        return self.__path

    def insert_around_cursor(self, __symbol_1: str, __symbol_2: str) -> None:
        cursor = self.textCursor()
        selected_text = cursor.selectedText()

        cursor.insertText(f"{selected_text}".join([__symbol_1, __symbol_2]))
        cursor.setPosition(cursor.position() - 1)
        self.setTextCursor(cursor)

    def pass_duplicate_symbol(self, __target: str) -> None | str:
        cursor = self.textCursor()

        if len(self.toPlainText().split("\n")[self.get_current_line()][cursor.positionInBlock():]) != 0:

            if self.toPlainText().split("\n")[self.get_current_line()][cursor.positionInBlock()] == __target:
                cursor.setPosition(cursor.position() + 1)
                self.setTextCursor(cursor)

            else:
                return "exception"

        else:
            return "exception"

    def get_last_word_of_current_line(self):
        ...

    def key_press_filter(
            self, __event,
            paren: bool = False,
            brace: bool = False,
            bracket: bool = False,
            quote_dbl: bool = False,
            apostrophe: bool = False,
            tag: bool = False
    ):

        self.lineNumberArea.update()

        if __event.key() == Qt.Key.Key_ParenLeft and paren:
            self.insert_around_cursor("(", ")")

        elif __event.key() == Qt.Key.Key_ParenRight and paren:
            if self.pass_duplicate_symbol(")") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_BraceLeft and brace:
            self.insert_around_cursor("{", "}")

        elif __event.key() == Qt.Key.Key_BraceRight and brace:
            if self.pass_duplicate_symbol("}") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_BracketLeft and bracket:
            self.insert_around_cursor("[", "]")

        elif __event.key() == Qt.Key.Key_BracketRight and bracket:
            if self.pass_duplicate_symbol("]") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_Less and tag:
            self.insert_around_cursor("<", ">")

        elif __event.key() == Qt.Key.Key_Greater and tag:
            if self.pass_duplicate_symbol(">") == "exception":
                super().keyPressEvent(__event)

        elif __event.key() == Qt.Key.Key_QuoteDbl and quote_dbl:
            self.insert_around_cursor('"', '"')

        elif __event.key() == Qt.Key.Key_Apostrophe and apostrophe:
            self.insert_around_cursor("'", "'")

        else:
            super().keyPressEvent(__event)
