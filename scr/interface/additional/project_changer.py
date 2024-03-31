from PySide6.QtWidgets import QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import QSize

from scr.interface.abstract import TransparentDialogWindow, ListChanger
from scr.interface.basic import Text, DialogButton

from scr.scripts.font import Font
from scr.scripts.tools.file import FileLoader

from scr.project.pyproject import PyProjectConfig
from scr.project import ImageGenerator, ProjectNameGenerator


class ProjectChanger(ListChanger):
    def __init__(self):
        super().__init__(*PyProjectConfig.get_projects_names())

        self.setStyleSheet(
            self.styleSheet() + FileLoader.load_style("scr/interface/additional/styles/project_changer.css")
        )

        self.setFont(Font.get_system_font("CascadiaMono.ttf", 12))
        self.__set_icons()

    def __set_icons(self) -> None:
        self.setIconSize(QSize(self.font().pointSize() * 2, self.font().pointSize() * 2))

        for item in self.get_items():
            icon = ImageGenerator.to_qicon(
                ImageGenerator.generate((300, 300), ProjectNameGenerator.get_basename(item.text()))
            )

            item.setIcon(icon)


class ProjectChangerWindow(TransparentDialogWindow):
    def __init__(self, __parent):
        super().__init__(__parent, width=1000, height=600)

        self.projectChanger = ProjectChanger()
        self.add_widget(Text.label("Projects...", "CascadiaMono.ttf", 9))
        self.add_widget(self.projectChanger)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.buttonsLayout.addWidget(DialogButton("Open", "accept"))
        self.buttonsLayout.addWidget(DialogButton("New", "reject"))
        self.buttonsLayout.addWidget(DialogButton("Cancel", "reject"))
        self.add_layout(self.buttonsLayout)
