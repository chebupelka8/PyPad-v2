from PySide6.QtWidgets import QWidget, QVBoxLayout


class AbstractSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.setMinimumWidth(800)
        self.setObjectName("settings-widget")

        self.setLayout(self.mainLayout)