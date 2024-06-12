import json
import os

from PIL import Image

from .file_checker import FileChecker


class FileLoader:

    @staticmethod
    def __load_any_text_file(__path: str) -> str:

        with open(os.path.normpath(__path), "r", encoding="utf-8") as file:
            result = file.read()

        return result

    @staticmethod
    def __load_any_bytes_file(__path: str) -> bytes:
        with open(os.path.normpath(__path), "rb") as file:
            result = file.read()

        return result

    @classmethod
    def load_text_file(cls, __path: str, *__extensions: str) -> str:
        FileChecker.verify_file_extensions(__path, *__extensions)

        return cls.__load_any_text_file(__path)

    @classmethod
    def load_text(cls, __path: str) -> str:
        return cls.__load_any_text_file(__path)

    @classmethod
    def load_style(cls, __path: str) -> str:
        FileChecker.verify_style_file(__path)

        return cls.__load_any_text_file(__path)

    @classmethod
    def load_json_text(cls, __path: str) -> str:
        FileChecker.verify_json_file(__path)

        return cls.__load_any_text_file(__path)

    @classmethod
    def load_html(cls, __path):
        FileChecker.verify_html_file(__path)

        return cls.__load_any_text_file(__path)

    @classmethod
    def load_python_file(cls, __path: str) -> str:
        FileChecker.verify_python_file(__path)

        return cls.__load_any_text_file(__path)

    @staticmethod
    def load_json(__path: str) -> dict:
        FileChecker.verify_json_file(__path)

        with open(os.path.normpath(__path), "r", encoding="utf-8") as file:
            result = json.load(file)

        return result

    @classmethod
    def load_image(cls, __path: str) -> Image:
        FileChecker.verify_file_extensions(__path, ".png", ".jpg", ".jpeg")

        with Image.open(os.path.normpath(__path)) as image:
            result = image

        return result
