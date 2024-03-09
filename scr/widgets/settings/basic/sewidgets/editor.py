from ...abstract import AbstractSettingsWidget, AbstractSettingFrame, FrameTitles

from scr.scripts.font import Font, EditorFontManager
from scr.scripts.settings import EditorSettingsUpdater


class EditorSettingsWidget(AbstractSettingsWidget):
    def __init__(self) -> None:
        super().__init__()

        self.font_family_changer = AbstractSettingFrame("Font Family", "Defines the font family")
        self.font_family_combo = self.font_family_changer.add_combobox(Font.get_all_font_families(), 200)
        self.font_family_combo.currentTextChanged.connect(lambda fam: EditorFontManager.set_current_font(family=fam))

        self.font_size_changer = AbstractSettingFrame("Font Size", "Defines the font size in pixels")
        self.font_size_spin = self.font_size_changer.add_spinbox((1, 100))
        self.font_size_spin.valueChanged.connect(lambda value: EditorFontManager.set_current_font(size=value))

        self.cursor_style_changer = AbstractSettingFrame("Cursor Style", "Defines the cursor style")
        self.cursor_style_combo = self.cursor_style_changer.add_combobox(["line", "block"])
        self.cursor_style_combo.currentTextChanged.connect(lambda style: EditorSettingsUpdater.set_cursor_style(style))

        self.tab_width_changer = AbstractSettingFrame("Tab Width", "Defines the tab width")
        self.tab_width_combo = self.tab_width_changer.add_combobox([str(i) for i in range(2, 9)], 50)
        self.tab_width_combo.currentTextChanged.connect(lambda wid: EditorSettingsUpdater.set_tab_width(int(wid)))

        self.update_values()

        self.mainLayout.addWidget(FrameTitles.title("Font Settings"))
        self.mainLayout.addWidget(self.font_family_changer)
        self.mainLayout.addWidget(self.font_size_changer)
        self.mainLayout.addWidget(FrameTitles.title("Cursor Settings"))
        self.mainLayout.addWidget(self.cursor_style_changer)
        self.mainLayout.addWidget(FrameTitles.title("Tab Settings"))
        self.mainLayout.addWidget(self.tab_width_changer)

    def update_values(self):
        self.font_family_combo.setCurrentText(EditorFontManager.get_current_family())
        self.font_size_spin.setValue(EditorFontManager.get_current_font_size())
        self.cursor_style_combo.setCurrentText(EditorSettingsUpdater.get_cursor_style())
        self.tab_width_combo.setCurrentText(str(EditorSettingsUpdater.get_tab_width()))
