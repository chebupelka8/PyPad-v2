from scr.interface.abstract import TransparentDialogWindow

from scr.scripts.tools.file import FileLoader

from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import Qt

from .basic import (
    SettingTree, MainSettingsWidget, EditorSettingsWidget,
    ThemeSettingsWidget, InfoWidget, InterpreterSettingsWidget
)


class SettingsMenu(TransparentDialogWindow):
    def __init__(self, __parent, restarter) -> None:
        super().__init__(__parent, "horizontal")

        self.restarter = restarter

        self.setWindowTitle("Settings")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(self.styleSheet() + FileLoader.load_style("scr/widgets/styles/settings_menu.css"))
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
            "Interpreter", lambda: self.settingsArea.setWidget(InterpreterSettingsWidget())
        )
        self.settingTree.connect_by_title(
            "About", lambda: self.settingsArea.setWidget(InfoWidget())
        )

        self.add_widget(self.settingTree, stretch=1)
        self.add_widget(self.settingsArea, stretch=3)
