from scr.scripts.tools.file import FileLoader
from scr.scripts.font import Font
from scr.configs.pics import IconPaths

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/welcome_screen.css"))
        self.setObjectName("welcome-screen")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logoLabel = self.__label()
        icon = QPixmap(IconPaths.SystemIcons.LOGO)
        logoLabel.setPixmap(icon)

        infoLabel = self.__label("""PyPad - is a code editor for different programming languages.
        PyPad supports some languages like a Python, Json, Html and CSS. So far,
        PyPad is in development and it is not suitable for use,
        but you can watch the demo version of the project and test it.""", 16)

        self.mainLayout.addWidget(logoLabel)
        self.mainLayout.addWidget(infoLabel)
        self.setLayout(self.mainLayout)

    @staticmethod
    def __label(__text: str | None = None, __font_size: int | None = None) -> QLabel:
        label = QLabel(__text) if __text is not None else QLabel()
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if __font_size is not None:
            label.setFont(Font.get_font_by_path("assets/fonts/CascadiaMono.ttf", __font_size))
        label.setWordWrap(True)

        return label
