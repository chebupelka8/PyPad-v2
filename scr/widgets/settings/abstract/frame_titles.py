from PySide6.QtWidgets import QLabel

from scr.interface.basic import Text


class FrameTitles:
    @staticmethod
    def title(__text: str) -> QLabel:
        return Text.label(__text, "CascadiaMono.ttf", 17, True)

    @staticmethod
    def subtitle(__text: str) -> QLabel:
        return Text.label(__text, "CascadiaMono.ttf", 14)

    @staticmethod
    def description(__text: str) -> QLabel:
        return Text.label(__text, "CascadiaMono.ttf", 10, word_wrap=True)
