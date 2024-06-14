from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from scr.configs.pics import IconPaths
from scr.project import VersionConfig

from ...abstract import AbstractSettingFrame, AbstractSettingsWidget


class InfoWidget(AbstractSettingsWidget):
    def __init__(self):
        super().__init__()

        label = QLabel()
        label.setPixmap(QPixmap(IconPaths.SystemIcons.LOGO))

        info_frame = AbstractSettingFrame(
            "Description",
            """
            <b>PyPad</b> - 
            is a code editor for different programming languages. 
            PyPad supports some languages like a Python, Json, Html and CSS. 
            So far, PyPad is in development and it is not suitable for use, but you can watch the demo 
            version of the project and test it.
            """,
        )
        hot_key_frame = AbstractSettingFrame(
            "Hot Keys",
            """Ctrl+O - Open directory\nCtrl+P - Open file\nCtrl+, - Open settings\nCtrl+T - Open theme picker\nCtrl+Tab - Switch current file""",
        )
        version_info_frame = AbstractSettingFrame(
            "Info",
            f"""
            <br>{VersionConfig.name}   by <a href={VersionConfig.author_social_link}>{VersionConfig.author}</a>
            <br>Version: {VersionConfig.version}
            <br>Build: {VersionConfig.build}
            <br>License: {VersionConfig.license}
            <br>Page: <a href={VersionConfig.project_page}>GitHub</a>
            """,
        )

        self.mainLayout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(info_frame)
        self.mainLayout.addWidget(hot_key_frame)
        self.mainLayout.addWidget(version_info_frame)
