import os

from scr.interface.additional import ThemeChangerWindow
from scr.scripts.tools.file import FileLoader

from ...abstract import AbstractSettingFrame, AbstractSettingsWidget, FrameTitles


class ThemeSettingsWidget(AbstractSettingsWidget):
    def __init__(self, __restarter) -> None:
        super().__init__()

        self.themeChanger = ThemeChangerWindow(self, __restarter)

        self.font_theme_changer = AbstractSettingFrame(
            "Color Theme", "Defines the current color theme"
        )
        self.change_theme = self.font_theme_changer.add_button(
            "Change color theme...", is_highlighted=True
        )
        self.change_theme.clicked.connect(self.show_theme_changer)

        self.add_widget(FrameTitles.title("Theme Settings"))
        self.add_widget(self.font_theme_changer)

    def show_theme_changer(self):
        themes = [
            FileLoader.load_json(f"scr/data/themes/{i}")["name"]
            for i in os.listdir("scr/data/themes")
        ]

        self.themeChanger.themeChanger.set_items(*themes)
        self.themeChanger.show()
