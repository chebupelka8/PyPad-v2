from PySide6.QtWidgets import QLabel, QFrame, QHBoxLayout

from scr.scripts.tools.file import FileLoader
from scr.scripts.utils import Path
from scr.project import ProjectConfig


class StatusBar(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/status_bar.css"))
        self.setObjectName("status-bar")
        self.setMinimumHeight(30)

        self.mainLayout = QHBoxLayout()

        self.current_file_status = QLabel()
        self.mainLayout.addWidget(self.current_file_status)

        self.setLayout(self.mainLayout)

    def set_current_file_status(self, __path: str) -> None:
        text = Path.to_relative_path(ProjectConfig.get_directory(), __path).replace("\\", "  >  ")
        self.current_file_status.setText(text)
