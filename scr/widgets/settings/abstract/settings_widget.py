from PySide6.QtWidgets import QWidget, QVBoxLayout


class AbstractSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.setMinimumWidth(800)
        self.setObjectName("settings-widget")

        self.setLayout(self.mainLayout)

    def add_widget(self, __widget) -> None:
        self.mainLayout.addWidget(__widget)

    def update_values(self) -> None:
        """
        Override this method
        """