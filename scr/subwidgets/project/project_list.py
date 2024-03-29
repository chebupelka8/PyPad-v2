from PySide6.QtWidgets import QHBoxLayout, QListWidget, QFrame, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

from scr.interface.additional import ListChanger
from scr.scripts.tools.file import FileLoader

from scr.project.pyproject import PyProjectConfig


class ProjectChanger(ListChanger):
    def __init__(self, __parent):
        super().__init__(__parent)

        self.set_items(*PyProjectConfig.get_projects_names())
