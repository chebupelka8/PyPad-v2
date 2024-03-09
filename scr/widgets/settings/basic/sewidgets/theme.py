from ...abstract import AbstractSettingsWidget, AbstractSettingFrame

from scr.interface.basic import UiTitles
from scr.subwidgets import ThemeChanger

from scr.scripts.tools.file import FileLoader


class ThemeSettingsWidget(AbstractSettingsWidget):
    def __init__(self, __restarter) -> None:
        super().__init__()

        self.themeChanger = ThemeChanger(self, restarter=__restarter)

        self.font_theme_changer = AbstractSettingFrame("Color Theme", "Defines the current color theme")
        self.change_theme = self.font_theme_changer.add_button("Change color theme...", is_highlighted=True)
        self.change_theme.clicked.connect(self.show_theme_changer)

        self.mainLayout.addWidget(UiTitles.title("Theme Settings"))
        self.mainLayout.addWidget(self.font_theme_changer)

    def show_theme_changer(self):
        themes = [FileLoader.load_json(f"scr/data/themes/{i}")["name"] for i in os.listdir("scr/data/themes")]

        self.themeChanger.set_items(*themes)
        self.themeChanger.show()
