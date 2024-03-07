from scr.exceptions import WrongFileExtension, NotFileError

import os


class FileChecker:

    @staticmethod
    def verify_file_extensions(__path: str, *__extensions):
        match __path:
            case path if not os.path.isfile(path):
                raise NotFileError(f"Argument must be a file, not directory")

            case path if not os.path.splitext(path)[1].lower() in __extensions:
                raise WrongFileExtension(f"File extension must be in {__extensions}")

    @staticmethod
    def check_exist(__path: str) -> bool:
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
        with open(__path, "r") as file:
            return file.readable()

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
        cls.verify_file_extensions(__path, ".png", ".jpg", ".jpeg")

    @classmethod
    def verify_file(cls, __path: str):
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
