import os

from scr.exceptions import NotFileError, WrongFileExtension


class FileChecker:

    @staticmethod
    def verify_file_extensions(__path: str, *__extensions):
        """
        Verifies if the file at the given path has one of the specified extensions.

        Parameters:
        __path (str): The path of the file to verify.
        *__extensions: Variable number of extensions to check against.

        Raises:
        NotFileError: If the path does not point to a file.
        WrongFileExtension: If the file extension is not in the specified extensions.

        Notes:
        - Checks if the file is a valid file and has one of the specified extensions.
        """

        match __path:
            case path if not os.path.isfile(path):
                raise NotFileError(f"Argument must be a file, not directory")

            case path if not os.path.splitext(path)[1].lower() in __extensions:
                raise WrongFileExtension(f"File extension must be in {__extensions}")

    @staticmethod
    def check_exist(__path: str) -> bool:
        """
        Checks if a file or directory exists at the specified path.

        Parameters:
        __path (str): The path to check for existence.

        Returns:
        bool: True if the file or directory exists, False otherwise.

        Notes:
        - Attempts to determine if a file or directory exists at the given path.
        """

        try:
            return os.path.exists(__path)

        except Exception:
            return False

    @staticmethod
    def is_python_file(__path: str) -> bool:
        return os.path.splitext(__path)[1].lower() == ".py"

    @staticmethod
    def is_html_file(__path: str) -> bool:
        return os.path.splitext(__path)[1].lower() == ".html"

    @staticmethod
    def is_json_file(__path: str) -> bool:
        return os.path.splitext(__path)[1].lower() == ".json"

    @staticmethod
    def is_text_file(__path: str) -> bool:
        return os.path.splitext(__path)[1].lower() in (".txt", ".md")

    @staticmethod
    def is_style_file(__path: str) -> bool:
        return os.path.splitext(__path)[1].lower() in (".qss", ".css")

    @staticmethod
    def is_picture_file(__path: str) -> bool:
        return os.path.splitext(__path)[1].lower() in (".jpg", ".jpeg", ".png", ".ico", ".gif")

    @staticmethod
    def is_readable(__path: str) -> bool:
        """
        Checks if a file is readable and not an image file.

        Parameters:
        __path (str): The path of the file to check.

        Returns:
        bool: True if the file is readable and not an image file, False otherwise.

        Notes:
        - Verifies if the file is readable and not an image file based on its extension.
        """

        if __path is None: return False

        with open(__path, "r") as file:
            return file.readable() and os.path.splitext(__path)[1] not in (".jpg", ".jpeg", ".png", ".ico", ".gif")

    @classmethod
    def verify_python_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".py")

    @classmethod
    def verify_json_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".json")

    @classmethod
    def verify_style_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".css", ".qss")

    @classmethod
    def verify_text_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".txt", ".md")

    @classmethod
    def verify_html_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".html")

    @classmethod
    def verify_picture_file(cls, __path: str):
        cls.verify_file_extensions(__path, ".jpg", ".jpeg", ".png", ".ico", ".gif")

    @classmethod
    def verify_file(cls, __path: str):
        """
        Verifies the file type based on its extension and performs corresponding verification.

        Parameters:
        __path (str): The path of the file to verify.

        Raises:
        WrongFileExtension: If the file extension is not supported.

        Notes:
        - Matches the file path extension to determine the file type and calls the respective verification method.
        """

        match __path:
            case path if cls.is_style_file(path):
                cls.verify_style_file(path)

            case path if cls.is_python_file(path):
                cls.verify_python_file(path)

            case path if cls.is_text_file(path):
                cls.verify_text_file(path)

            case path if cls.is_json_file(path):
                cls.verify_json_file(path)

            case path if cls.is_picture_file(path):
                cls.verify_picture_file(path)

            case _:
                raise WrongFileExtension("PyPad can't open this file")
