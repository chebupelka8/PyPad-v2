from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QFrame, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)

from scr.configs.pics import IconPaths
from scr.scripts.tools.file import FileLoader


class SideBarButton(QPushButton):
    def __init__(self, __path_to_icon: str) -> None:
        super().__init__()

        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setFixedSize(30, 30)
        self.setIcon(QPixmap(__path_to_icon))
        self.setIconSize(self.iconSize() * 1.2)


class SideBar(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/side_bar.css"))
        self.setObjectName("side-bar")

        self.setMaximumWidth(50)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.menuAppsBtn = SideBarButton(IconPaths.SystemIcons.APPS)
        self.mainLayout.addWidget(self.menuAppsBtn)

        self.fileTreeOpenerBtn = SideBarButton(IconPaths.SystemIcons.FOLDER_OPEN)
        self.mainLayout.addWidget(self.fileTreeOpenerBtn)

        self.searchBtn = SideBarButton(IconPaths.SystemIcons.SEARCH)
        self.mainLayout.addWidget(self.searchBtn)

        self.mainLayout.addItem(QSpacerItem(30, 0, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding))

        self.runFileBtn = SideBarButton(IconPaths.SystemIcons.RUN)
        self.mainLayout.addWidget(self.runFileBtn)

        self.openSettingsBtn = SideBarButton(IconPaths.SystemIcons.SETTINGS)
        self.mainLayout.addWidget(self.openSettingsBtn)

    def file_tree_opener_connect(self, __command) -> None:
        self.fileTreeOpenerBtn.clicked.connect(__command)

    def settings_opener_connect(self, __command) -> None:
        self.openSettingsBtn.clicked.connect(__command)
