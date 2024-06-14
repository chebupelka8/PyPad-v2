from ...utils import from_multiple


class CodeAnalyzer:
    @staticmethod
    def find_tabs_in_string(string: str, __cursor_index: int) -> int:
        """
        Finds the number of tabs in a string up to a specified cursor index.

        Parameters:
        string (str): The input string.
        __cursor_index (int): The cursor index to search until.

        Returns:
        int: The number of tabs found.

        Notes:
        - Iterates through the string up to the cursor index to count tabs.
        """

        res = 0

        for i, letter in enumerate(string):
            if letter == "\t" and i < __cursor_index:
                res += 1

            else:
                break

        return res

    @staticmethod
    def find_tabs_in_string_by_spaces(
        string, __cursor_index: int, __tab_count: int = 4
    ) -> int:
        """
        Finds the number of tabs in a string based on spaces up to a specified cursor index.

        Parameters:
        string: The input string.
        __cursor_index (int): The cursor index to search until.
        __tab_count (int): The number of spaces per tab.

        Returns:
        int: The number of tabs found based on spaces.

        Notes:
        - Counts tabs based on spaces up to the cursor index and tab width.
        """

        res = 0

        for i, letter in enumerate(string):
            if letter == " " and i < __cursor_index:
                res += 1

            else:
                break

        return res // __tab_count

    @staticmethod
    def get_index_first_symbol_of_line(__line: str) -> int:
        """
        Finds the index of the first non-space character in a line.

        Parameters:
        __line (str): The line to search.

        Returns:
        int: The index of the first non-space character.

        Notes:
        - Iterates through the line to find the index of the first non-space character.
        """

        for i, letter in enumerate(__line):
            if letter != " ":
                return i

    @classmethod
    def get_tab_width_by_text(cls, __text: str) -> int | None:
        """
        Determines the tab width based on the text content.

        Parameters:
        __text (str): The text content to analyze.

        Returns:
        int | None: The calculated tab width or None if not found.

        Notes:
        - Analyzes the text to infer the tab width used in the content.
        """

        res = []

        for line in __text.split("\n"):
            count = line.count(" ", 0, cls.get_index_first_symbol_of_line(line))
            if count > 1:
                res.append(count)

        return from_multiple(res, [i for i in range(2, 9)])

    @staticmethod
    def refactor_spaces_to_tabs(__text: str, __tab_width: int) -> str:
        """
        Converts spaces to tabs based on the specified tab width.

        Parameters:
        __text (str): The text to refactor.
        __tab_width (int): The tab width to use for conversion.

        Returns:
        str: The text with spaces converted to tabs.

        Notes:
        - Replaces spaces with tabs in the text based on the tab width.
        """

        if __tab_width is None or __tab_width == 0:
            return __text

        return __text.replace(" " * __tab_width, "\t")

    @staticmethod
    def check_last_character_is_colon(string: str) -> int:
        """
        Checks if the last character of a string is a colon.

        Parameters:
        string (str): The string to check.

        Returns:
        int: 1 if the string ends with ':', 0 otherwise.

        Notes:
        - Returns 1 if the string ends with a colon, 0 otherwise.
        """

        try:
            return 1 if string.rstrip()[-1] == ":" else 0
        except IndexError:
            return 0
