from scr.interface.additional import AbstractWindow, TransparentDialogWindow

from scr.scripts.tools.file import FileLoader

from PySide6.QtWidgets import QScrollArea, QHBoxLayout
from PySide6.QtCore import Qt

from .basic import SettingTree, MainSettingsWidget, EditorSettingsWidget, ThemeSettingsWidget, InfoWidget


class SettingsMenuWidget(AbstractWindow):
    def __init__(self, restarter) -> None:
        super().__init__()

        self.restarter = restarter

        self.setWindowTitle("Settings")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/settings_menu.css"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.settingsArea = QScrollArea()
        self.settingsArea.setMinimumWidth(800)
        self.settingsArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.settingsArea.setWidget(MainSettingsWidget())

        self.settingTree = SettingTree()
        self.settingTree.connect_by_title(
            "General", lambda: self.settingsArea.setWidget(MainSettingsWidget())
        )
        self.settingTree.connect_by_title(
            "Editor", lambda: self.settingsArea.setWidget(EditorSettingsWidget())
        )
        self.settingTree.connect_by_title(
            "Theme", lambda: self.settingsArea.setWidget(ThemeSettingsWidget(self.restarter))
        )
        self.settingTree.connect_by_title(
            "About", lambda: self.settingsArea.setWidget(InfoWidget())
        )

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.settingTree, stretch=1)
        self.mainLayout.addWidget(self.settingsArea, stretch=3)

        self.setLayout(self.mainLayout)


class SettingsMenu(TransparentDialogWindow):
    def __init__(self, __parent, restarter) -> None:
        super().__init__(__parent)

        self.mainLayout = QHBoxLayout()
        self.menuWidget = SettingsMenuWidget(restarter)
        self.mainLayout.addWidget(self.menuWidget)

        self.setLayout(self.mainLayout)