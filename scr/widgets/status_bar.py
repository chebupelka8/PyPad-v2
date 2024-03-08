from PySide6.QtWidgets import QLabel, QFrame, QHBoxLayout, QSpacerItem, QSizePolicy

from scr.scripts.tools.file import FileLoader
from scr.scripts.font import Font, WorkbenchFontManager
from scr.scripts.utils import Path
from scr.project import ProjectConfig, VersionConfig


class StatusBar(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/status_bar.css"))
        self.setObjectName("status-bar")
        self.setMinimumHeight(30)

        self.mainLayout = QHBoxLayout()

        self.__main_font = Font.get_system_font(
            WorkbenchFontManager.get_current_family(), WorkbenchFontManager.get_current_font_size()
        )

        self.current_file_status = QLabel()
        self.current_position = QLabel()
        self.version_info = QLabel(f"Build: {VersionConfig.build} Version: {VersionConfig.version}")
        # self.current_encoding = QLabel("utf-8")

        self.update_font()

        self.mainLayout.addWidget(self.current_file_status)
        self.mainLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored))
        self.mainLayout.addWidget(self.current_position)
        self.mainLayout.addItem(QSpacerItem(30, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Ignored))
        self.mainLayout.addWidget(self.version_info)
        # self.mainLayout.addWidget(self.current_encoding)

        self.setLayout(self.mainLayout)

    def update_font(self) -> None:
        self.__main_font = Font.get_system_font(
            WorkbenchFontManager.get_current_family(), WorkbenchFontManager.get_current_font_size() * 0.8
        )
        self.current_position.setFont(self.__main_font)
        self.current_file_status.setFont(self.__main_font)
        self.version_info.setFont(self.__main_font)

    def set_current_file_status(self, __path: str) -> None:
        text = Path.to_relative_path(ProjectConfig.get_directory(), __path).replace("\\", " > ")
        self.current_file_status.setText(text)

    def set_current_position(self, line: int, char: int) -> None:
        self.current_position.setText(f"Line: {line + 1}{" " * 3}Column: {char + 1}")

    def text_file(self, visible: bool) -> None:
        self.current_position.setVisible(visible)
        # self.current_encoding.setVisible(visible)

    def change_file_status(self, tab) -> None:
        if tab is None: return

        if tab.path is not None:
            self.set_current_file_status(tab.path)

        else:
            self.set_current_file_status(tab.title)

    def update_status_bar(self, tab) -> None:
        if tab is None: return

        if tab.is_readable(): self.text_file(True)
        else: self.text_file(False)
