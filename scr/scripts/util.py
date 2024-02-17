import os
import sys

from PySide6.QtGui import QFontDatabase, QFont


def restart_application() -> None:
    os.execv(sys.executable, ['python'] + sys.argv)


def smallest_multiple(lst) -> int | None:
    def is_multiple(num):
        return num % 2 == 0 or num % 3 == 0 or num % 4 == 0 or num % 8 == 0

    return min(lst, key=lambda x: (is_multiple(x), x) if is_multiple(x) else None)


def from_multiple(__array: list[int], __for: list[int]) -> int | None:
    if len(__array) == 0:
        return

    for i in __for:
        if all(map(lambda x: x % i == 0, __array)) and min(__array) == i:
            return i


class Font:
    @staticmethod
    def get_all_font_families() -> list[str]:
        return QFontDatabase.families()

    @staticmethod
    def get_font_by_path(__path: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        __id = QFontDatabase.addApplicationFont(__path)
        families = QFontDatabase.applicationFontFamilies(__id)

        font = QFont(families[0], __size, 1, __italic)
        font.setBold(__bold)

        return font

    @staticmethod
    def get_system_font(__family: str, __size: int | float, __bold: bool = False, __italic: bool = False) -> QFont:
        font = QFont(__family, __size, 1, __italic)
        font.setBold(__bold)

        return font
