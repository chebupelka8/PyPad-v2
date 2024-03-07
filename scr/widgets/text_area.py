from scr.scripts import FileLoader, FileChecker, EditorFontManager, Font, EditorSettingsUpdater, CodeAnalyzer
from scr.config import TextEditorTheme
from .code_map import CodeGlanceMap

from PySide6.QtWidgets import QPlainTextEdit, QTextEdit, QWidget, QHBoxLayout
from PySide6.QtGui import QColor, QTextFormat, QPainter, QPalette, QFontMetrics
from PySide6.QtCore import Qt, QRect, QSize, QPoint


class TextEditorArea(QPlainTextEdit):
    def __init__(self, __path: str | None = None):
        super().__init__()

        # setup style sheet
        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/editor_area.css"))
        self.setObjectName("text-area")

        # self setup
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # font setup
        self.__main_font = Font.get_system_font(*EditorFontManager.get_current_font().values())
        self.setFont(self.__main_font)

        # layout for code glancing
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        self.__path = __path

        if __path is not None and FileChecker.is_readable(__path):
            text = FileLoader.load_text(__path)
            text = CodeAnalyzer.refactor_spaces_to_tabs(
                text, CodeAnalyzer.get_tab_width_by_text(text)
            )
            self.insertPlainText(text)
            self.codeMap = CodeGlanceMap(text, self.__main_font)
            self.textChanged.connect(self.__test)
            self.mainLayout.addWidget(self.codeMap, alignment=Qt.AlignmentFlag.AlignRight)

        # vars
        self.__cursor_style = EditorSettingsUpdater.get_cursor_style()
        self.__tab_width = EditorSettingsUpdater.get_tab_width()

        # color setup
        self.set_default_text_color(TextEditorTheme.DEFAULT)

        # instances
        self.lineNumberArea = LineNumPaint(self)

        # connections
        self.__highlight_current_line()
        self.__update_line_number_area_width()
        self.__update_cursor_width()
        self.update_settings()

        self.blockCountChanged.connect(self.__update_line_number_area_width)
        self.cursorPositionChanged.connect(self.__update_current_line)
        self.cursorPositionChanged.connect(self.__highlight_current_line)
        self.cursorPositionChanged.connect(self.__update_cursor_width)
        self.textChanged.connect(self.__highlight_current_line)
        self.textChanged.connect(self.__update_cursor_width)
        self.verticalScrollBar().valueChanged.connect(self.__scroll_updating)

        # variables
        self.__current_line = 0

    def __test(self) -> None:
        # just testing function
        # there is bug with code map scrolling, when you type text
        self.codeMap.setPlainText(self.toPlainText())
        self.codeMap.verticalScrollBar().setValue(self.verticalScrollBar().value())

    def __scroll_updating(self) -> None:
        self.lineNumberArea.update()

        division = self.codeMap.get_pixel_size()
        self.codeMap.verticalScrollBar().setValue(self.verticalScrollBar().value() / division)

    def __update_cursor_width(self):
        if self.__cursor_style == "block":
            cursor = self.textCursor()

            try:
                symbol = cursor.block().text()[cursor.positionInBlock()]
                if symbol == "\t": symbol = " "
            except IndexError:
                symbol = " "

            self.setCursorWidth(QFontMetrics(self.__main_font).horizontalAdvanceChar(symbol))

        else:
            self.setCursorWidth(1)

    def update_font(self):
        self.__main_font = Font.get_system_font(*EditorFontManager.get_current_font().values())
        self.setFont(self.__main_font)
        self.codeMap.set_font(self.__main_font)

        self.__update_line_number_area_width()

    def update_settings(self):
        self.__cursor_style = EditorSettingsUpdater.get_cursor_style()
        self.__update_cursor_width()

        self.__tab_width = EditorSettingsUpdater.get_tab_width()
        self.setTabStopDistance(QFontMetrics(self.__main_font).horizontalAdvanceChar(" ") * self.__tab_width)

    def get_current_tab_width(self) -> int:
        return self.__tab_width

    def get_full_path(self):
        return self.__path

    def get_line_count(self) -> int:
        return self.toPlainText().count("\n")

    def set_default_text_color(self, __color: str) -> None:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Text, QColor(__color))
        self.setPalette(palette)

    def wheelEvent(self, delta) -> None:
        self.lineNumberArea.update()
        super().wheelEvent(delta)

    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)

        self.update()
        self.lineNumberArea.update()
        self.__highlight_current_line()
        self.__update_cursor_width()

    def keyPressEvent(self, event):
        self.lineNumberArea.update()

        super().keyPressEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        content_rect = self.contentsRect()
        self.lineNumberArea.setGeometry(
            QRect(content_rect.left(), content_rect.top(), self.get_number_area_width(), content_rect.height())
        )

    def get_current_line(self) -> int:
        return self.__current_line

    def get_current_line_text(self) -> str:
        return self.toPlainText().split("\n")[self.__current_line]

    def get_text_before_cursor(self) -> str:
        return self.toPlainText()[:self.textCursor().position()]

    def __update_line_number_area_width(self):
        margins = self.viewportMargins()
        self.setViewportMargins(self.get_number_area_width(), margins.top(), 160, margins.bottom())

    def get_number_area_width(self) -> int:
        block_count = self.document().blockCount()
        max_value = max(1, block_count)
        d_count = len(str(max_value))
        width = self.fontMetrics().height() * d_count + 5

        return width

    def __highlight_current_line(self):
        extra_selections = []

        if not self.isReadOnly() and self.hasFocus():
            selection = QTextEdit.ExtraSelection()

            selection.format.setBackground(QColor("#303030"))
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()

            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def __update_current_line(self):
        cursor = self.textCursor()
        self.__current_line = cursor.blockNumber()

    def line_number_area_paint_event(self, event):
        cursor = self.textCursor()
        painter = QPainter(self.lineNumberArea)

        painter.fillRect(event.rect(), QColor("#272727"))
        line_height = self.fontMetrics().lineSpacing()

        block_number = self.cursorForPosition(QPoint(0, int(line_height / 2))).blockNumber()
        first_visible_block = self.document().findBlock(block_number)
        cursor.setPosition(self.cursorForPosition(QPoint(0, int(line_height / 2))).position())
        rect = self.cursorRect()
        scroll_compensation = rect.y() - int(rect.y() / line_height) * line_height
        top = scroll_compensation
        last_block_number = self.cursorForPosition(QPoint(0, self.height() - 1)).blockNumber()

        height = self.fontMetrics().height()
        block = first_visible_block

        while block.isValid() and (top <= event.rect().bottom()) and block_number <= last_block_number:
            if block.isVisible():
                number = str(block_number + 1)
                painter.setFont(self.__main_font)
                painter.setPen(QColor("#7f7f7f"))

                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignCenter, number)

            block = block.next()
            top = top + line_height
            block_number += 1


class LineNumPaint(QWidget):
    def __init__(self, parent: TextEditorArea):
        super().__init__(parent)

        self.setObjectName("number-area")

        self.edit_line_num = parent

    def sizeHint(self):
        return QSize(self.edit_line_num.get_number_area_width(), 0)

    def paintEvent(self, event):
        self.edit_line_num.line_number_area_paint_event(event)
