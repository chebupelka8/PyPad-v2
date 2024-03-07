from ...utils import from_multiple


class CodeAnalyzer:

    @staticmethod
    def find_tabs_in_string(string: str, __cursor_index: int) -> int:
        res = 0

        for i, letter in enumerate(string):
            if letter == "\t" and i < __cursor_index:
                res += 1

            else:
                break

        return res

    @staticmethod
    def find_tabs_in_string_by_spaces(string, __cursor_index: int, __tab_count: int = 4) -> int:
        res = 0

        for i, letter in enumerate(string):
            if letter == " " and i < __cursor_index:
                res += 1

            else:
                break

        return res // __tab_count

    @staticmethod
    def get_index_first_symbol_of_line(__line: str) -> int:
        for i, letter in enumerate(__line):
            if letter != " ": return i

    @classmethod
    def get_tab_width_by_text(cls, __text: str) -> int | None:
        res = []

        for line in __text.split("\n"):
            count = line.count(" ", 0, cls.get_index_first_symbol_of_line(line))
            if count > 1: res.append(count)

        return from_multiple(res, [i for i in range(2, 9)])

    @staticmethod
    def refactor_spaces_to_tabs(__text: str, __tab_width: int) -> str:
        if __tab_width is None or __tab_width == 0:
            return __text

        return __text.replace(" " * __tab_width, "\t")

    @staticmethod
    def check_last_character_is_colon(string: str) -> int:
        """This function returns 1 if the string ends with ':' else 0"""

        try:
            return 1 if string.rstrip()[-1] == ":" else 0
        except IndexError:
            return 0