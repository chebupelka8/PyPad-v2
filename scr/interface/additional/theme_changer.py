from scr.scripts.theme import ThemeManager

from scr.interface.basic import Text, DialogButton
from scr.interface.abstract import ListChanger, TransparentDialogWindow

from PySide6.QtWidgets import QHBoxLayout, QSpacerItem, QSizePolicy

from .restarter import Restarter


class ThemeChanger(ListChanger):
    def __init__(self, restarter: Restarter) -> None:
        super().__init__()

        self.restarter = restarter
        self.itemDoubleClicked.connect(self.use)

    def change_theme(self, __name: str) -> None:
        # self.close()

        ThemeManager.set_current_theme_by_name(__name)

        self.restarter.set_command_after_restart(ThemeManager.save)
        self.restarter.show()

    def open(self):
        self.setCurrentItem(self.get_item_by_text(ThemeManager.get_current_theme_name()))

    def use(self):
        self.change_theme(self.get_current_item().text())


class ThemeChangerWindow(TransparentDialogWindow):
    def __init__(self, __parent, __restarter: Restarter) -> None:
        super().__init__(__parent)

        self.themeChanger = ThemeChanger(__restarter)
        self.add_widget(Text.label("Themes...", "CascadiaMono.ttf", 9))
        self.add_widget(self.themeChanger)

        # buttons
        self.acceptBtn = DialogButton("Accept", "accept")
        self.rejectBtn = DialogButton("Cancel", "reject")
        self.acceptBtn.clicked.connect(self.accept)
        self.rejectBtn.clicked.connect(self.reject)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.buttonsLayout.addWidget(self.acceptBtn)
        self.buttonsLayout.addWidget(self.rejectBtn)
        self.add_layout(self.buttonsLayout)

    def accept(self):
        self.themeChanger.use()

    def show(self):
        super().show()
        self.themeChanger.open()
