from scr.scripts import EditorFontManager, FileLoader, Font, WorkbenchFontManager, EditorSettingsUpdater
from scr.subwidgets import ThemeChanger
from scr.interface.basic import UiTitles
from scr.interface.additional import TransparentDialogWindow, AbstractWindow

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QComboBox, QLabel,
    QSpinBox, QFrame, QListWidget, QPushButton,
    QScrollArea, QWidget
)
from PySide6.QtCore import Qt

import os


class _SettingFrame(QFrame):
    def __init__(self, __title: str, __description: str) -> None:
        super().__init__()

        self.setObjectName("setting-frame")
        self.mainLayout = QVBoxLayout()
        self.setMinimumHeight(100)
        self.setContentsMargins(10, 0, 0, 0)

        self.add_subtitle(__title)
        self.add_description(__description)

        self.setLayout(self.mainLayout)

    def add_subtitle(self, __text: str) -> None:
        self.mainLayout.addWidget(UiTitles.subtitle(__text))

    def add_description(self, __text: str) -> None:
        self.mainLayout.addWidget(UiTitles.description(__text))

    def add_combobox(self, __values: list, __width: int = 200, *, should_return: bool = True) -> QComboBox | None:
        combobox = QComboBox()
        combobox.addItems(__values)
        combobox.setFixedWidth(__width)
        combobox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        combobox.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.mainLayout.addWidget(combobox)

        return combobox if should_return else None

    def add_spinbox(
            self,
            __range: tuple[int, int], __width: int = 30,
            __buttons: bool = False, *, should_return: bool = True
    ) -> None | QSpinBox:

        spinbox = QSpinBox()
        spinbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        spinbox.setRange(*__range)
        spinbox.setFixedWidth(__width)
        spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.mainLayout.addWidget(spinbox)

        return spinbox if should_return else None

    def add_link(self, __text: str):
        label = QLabel(f'<a href="#">{__text}</a>')
        self.mainLayout.addWidget(label)

        return label

    def add_button(self, __text: str, __width: int = 200, is_highlighted: bool = False):
        btn = QPushButton(__text)
        btn.setFixedWidth(__width)
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        if is_highlighted: btn.setObjectName("highlighted-btn")

        self.mainLayout.addWidget(btn)

        return btn


class _SettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.setMinimumWidth(800)
        self.setObjectName("settings-widget")

        self.setLayout(self.mainLayout)


class MainSettingsWidget(_SettingsWidget):
    def __init__(self) -> None:
        super().__init__()

        self.font_family_changer = _SettingFrame("Font Family", "Defines the font family")
        self.font_family_combo = self.font_family_changer.add_combobox(Font.get_all_font_families(), 200)
        self.font_family_combo.currentTextChanged.connect(lambda fam: WorkbenchFontManager.set_current_font(family=fam))

        self.font_size_changer = _SettingFrame("Font Size", "Defines the font size in pixels")
        self.font_size_spin = self.font_size_changer.add_spinbox((1, 100))
        self.font_size_spin.valueChanged.connect(lambda value: WorkbenchFontManager.set_current_font(size=value))

        self.update_values()

        self.mainLayout.addWidget(UiTitles.title("Font Settings"))
        self.mainLayout.addWidget(self.font_family_changer)
        self.mainLayout.addWidget(self.font_size_changer)

    def update_values(self):
        self.font_family_combo.setCurrentText(WorkbenchFontManager.get_current_family())
        self.font_size_spin.setValue(WorkbenchFontManager.get_current_font_size())


class EditorSettingsWidget(_SettingsWidget):
    def __init__(self) -> None:
        super().__init__()

        self.font_family_changer = _SettingFrame("Font Family", "Defines the font family")
        self.font_family_combo = self.font_family_changer.add_combobox(Font.get_all_font_families(), 200)
        self.font_family_combo.currentTextChanged.connect(lambda fam: EditorFontManager.set_current_font(family=fam))

        self.font_size_changer = _SettingFrame("Font Size", "Defines the font size in pixels")
        self.font_size_spin = self.font_size_changer.add_spinbox((1, 100))
        self.font_size_spin.valueChanged.connect(lambda value: EditorFontManager.set_current_font(size=value))

        self.cursor_style_changer = _SettingFrame("Cursor Style", "Defines the cursor style")
        self.cursor_style_combo = self.cursor_style_changer.add_combobox(["line", "block"])
        self.cursor_style_combo.currentTextChanged.connect(lambda style: EditorSettingsUpdater.set_cursor_style(style))

        self.tab_width_changer = _SettingFrame("Tab Width", "Defines the tab width")
        self.tab_width_combo = self.tab_width_changer.add_combobox([str(i) for i in range(2, 9)], 50)
        self.tab_width_combo.currentTextChanged.connect(lambda wid: EditorSettingsUpdater.set_tab_width(int(wid)))

        self.update_values()

        self.mainLayout.addWidget(UiTitles.title("Font Settings"))
        self.mainLayout.addWidget(self.font_family_changer)
        self.mainLayout.addWidget(self.font_size_changer)
        self.mainLayout.addWidget(UiTitles.title("Cursor Settings"))
        self.mainLayout.addWidget(self.cursor_style_changer)
        self.mainLayout.addWidget(UiTitles.title("Tab Settings"))
        self.mainLayout.addWidget(self.tab_width_changer)

    def update_values(self):
        self.font_family_combo.setCurrentText(EditorFontManager.get_current_family())
        self.font_size_spin.setValue(EditorFontManager.get_current_font_size())
        self.cursor_style_combo.setCurrentText(EditorSettingsUpdater.get_cursor_style())
        self.tab_width_combo.setCurrentText(str(EditorSettingsUpdater.get_tab_width()))


class ThemeSettingsWidget(_SettingsWidget):
    def __init__(self, __restarter) -> None:
        super().__init__()

        self.themeChanger = ThemeChanger(self, restarter=__restarter)

        self.font_theme_changer = _SettingFrame("Color Theme", "Defines the current color theme")
        self.change_theme = self.font_theme_changer.add_button("Change color theme...", is_highlighted=True)
        self.change_theme.clicked.connect(self.show_theme_changer)

        self.mainLayout.addWidget(UiTitles.title("Theme Settings"))
        self.mainLayout.addWidget(self.font_theme_changer)

    def show_theme_changer(self):
        themes = [FileLoader.load_json(f"scr/data/themes/{i}")["name"] for i in os.listdir("scr/data/themes")]

        self.themeChanger.add_items(*themes)
        self.themeChanger.show()


class SettingTree(QListWidget):
    def __init__(self):
        super().__init__()

        self.update_font()

        self.addItems(["General", "Editor", "Theme"])
        self.setCurrentRow(0)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.__commands: dict = {}
        self.currentTextChanged.connect(self.__connection)

        WorkbenchFontManager.add_font_updater(self.update_font)

    def update_font(self) -> None:
        self.__main_font = Font.get_system_font(
            WorkbenchFontManager.get_current_family(), WorkbenchFontManager.get_current_font_size()
        )
        self.setFont(self.__main_font)

    def connect_by_title(self, __title: str, __command):
        try:
            self.__commands[__title] = __command

        except TypeError:
            ...

    def __connection(self, __text):
        if __text not in list(self.__commands.keys()): return

        self.__commands[__text]()


class SettingsMenuWidget(AbstractWindow):
    def __init__(self, restarter) -> None:
        super().__init__()

        self.restarter = restarter

        self.setWindowTitle("Settings")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(FileLoader.load_style("scr/styles/settings_menu.css"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.settingsArea = QScrollArea()
        self.settingsArea.setMinimumWidth(800)
        self.settingsArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.settingsArea.setWidget(MainSettingsWidget())

        self.settingTree = SettingTree()
        self.settingTree.connect_by_title(
            "Main", lambda: self.settingsArea.setWidget(MainSettingsWidget())
        )
        self.settingTree.connect_by_title(
            "Editor", lambda: self.settingsArea.setWidget(EditorSettingsWidget())
        )

        self.settingTree.connect_by_title(
            "Theme", lambda: self.settingsArea.setWidget(ThemeSettingsWidget(self.restarter))
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
