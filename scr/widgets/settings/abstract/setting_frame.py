from PySide6.QtWidgets import QFrame, QVBoxLayout, QComboBox, QSpinBox, QLabel, QPushButton
from PySide6.QtCore import Qt

from .frame_titles import FrameTitles

from typing import Optional


class AbstractSettingFrame(QFrame):
    def __init__(self, __title: Optional[str], __description: Optional[str]) -> None:
        super().__init__()

        self.setObjectName("setting-frame")
        self.mainLayout = QVBoxLayout()
        self.setMinimumHeight(100)
        self.setContentsMargins(10, 0, 0, 0)

        if __title is not None: self.add_subtitle(__title)
        if __description is not None: self.add_description(__description)

        self.setLayout(self.mainLayout)

    def add_subtitle(self, __text: str) -> None:
        self.mainLayout.addWidget(FrameTitles.subtitle(__text))

    def add_description(self, __text: str) -> None:
        self.mainLayout.addWidget(FrameTitles.description(__text))

    def add_combobox(self, __values: list, __width: int = 200, *, should_return: bool = True) -> QComboBox | None:
        combobox = QComboBox()
        combobox.addItems(__values)
        combobox.setFixedWidth(__width)
        combobox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        combobox.view().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.mainLayout.addWidget(combobox)

        return combobox if should_return else None

    def add_spinbox(
            self,
            __range: tuple[int, int], __width: int = 30,
            __buttons: bool = False, *, should_return: bool = True
    ) -> None | QSpinBox:

        spinbox = QSpinBox()
        spinbox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        spinbox.setRange(*__range)
        spinbox.setFixedWidth(__width)
        spinbox.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

        self.mainLayout.addWidget(spinbox)

        return spinbox if should_return else None

    def add_link(self, __text: str):
        label = QLabel(f'<a href="#">{__text}</a>')
        self.mainLayout.addWidget(label)

        return label

    def add_button(self, __text: str, __width: int = 200, is_highlighted: bool = False):
        btn = QPushButton(__text)
        btn.setFixedWidth(__width)
        btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        if is_highlighted: btn.setObjectName("highlighted-btn")

        self.mainLayout.addWidget(btn)

        return btn
