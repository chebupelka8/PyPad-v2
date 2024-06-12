from typing import Any, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QPushButton, QVBoxLayout

from .frame_titles import FrameTitles


class AbstractSettingFrame(QFrame):
    def __init__(self, __title: Optional[str], __description: Optional[str]) -> None:
        super().__init__()

        self.setObjectName("setting-frame")
        self.mainLayout = QVBoxLayout()
        self.setMinimumHeight(100)
        self.setContentsMargins(10, 0, 0, 0)

        if __title is not None:
            self.__add_subtitle(__title)
        if __description is not None:
            self.__add_description(__description)

        self.setLayout(self.mainLayout)

    def __add_subtitle(self, __text: str) -> None:
        self.mainLayout.addWidget(FrameTitles.subtitle(__text))

    def __add_description(self, __text: str) -> None:
        self.mainLayout.addWidget(FrameTitles.description(__text))

    def add_widget(self, __widget) -> Any:
        self.mainLayout.addWidget(__widget)
        return __widget

    def add_button(self, __text: str, __width: int = 200, is_highlighted: bool = False):
        btn = QPushButton(__text)
        btn.setFixedWidth(__width)
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        if is_highlighted:
            btn.setObjectName("highlighted-btn")

        self.mainLayout.addWidget(btn)

        return btn
