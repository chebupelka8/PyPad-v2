from ...abstract import AbstractSettingsWidget, AbstractSettingFrame

from scr.interface.basic import UiTitles
from scr.scripts.font import Font, WorkbenchFontManager


class MainSettingsWidget(AbstractSettingsWidget):
    def __init__(self) -> None:
        super().__init__()

        self.font_family_changer = AbstractSettingFrame("Font Family", "Defines the font family")
        self.font_family_combo = self.font_family_changer.add_combobox(Font.get_all_font_families(), 200)
        self.font_family_combo.currentTextChanged.connect(lambda fam: WorkbenchFontManager.set_current_font(family=fam))

        self.font_size_changer = AbstractSettingFrame("Font Size", "Defines the font size in pixels")
        self.font_size_spin = self.font_size_changer.add_spinbox((1, 100))
        self.font_size_spin.valueChanged.connect(lambda value: WorkbenchFontManager.set_current_font(size=value))

        self.update_values()

        self.mainLayout.addWidget(UiTitles.title("Font Settings"))
        self.mainLayout.addWidget(self.font_family_changer)
        self.mainLayout.addWidget(self.font_size_changer)
        # self.mainLayout.addWidget(UiTitles.title("Icons"))

    def update_values(self):
        self.font_family_combo.setCurrentText(WorkbenchFontManager.get_current_family())
        self.font_size_spin.setValue(WorkbenchFontManager.get_current_font_size())