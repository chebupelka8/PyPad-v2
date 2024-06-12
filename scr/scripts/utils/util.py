import os
import sys


def restart_application() -> None:
    os.execv(sys.executable, ["python"] + sys.argv)


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
