from PySide6.QtWidgets import QHBoxLayout

from scr.interface.additional import TransparentDialogWindow, AbstractWindow


class ProjectListWidget(AbstractWindow):
    def __init__(self) -> None:
        super().__init__()


class ProjectListWindow(TransparentDialogWindow):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(ProjectListWidget())
        self.setLayout(self.mainLayout)

