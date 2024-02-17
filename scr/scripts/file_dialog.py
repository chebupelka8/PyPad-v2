from PySide6.QtWidgets import QFileDialog

import os


class FileDialog:

    @staticmethod
    def get_open_file_name():
        path = QFileDialog.getOpenFileName()[0]

        if not os.path.exists(path):
            print("Warning: {File not found}")
            return

        return path

    @staticmethod
    def get_open_directory():
        path = QFileDialog.getExistingDirectory()

        if not os.path.exists(path):
            print("Warning: {Directory not found}")
            return

        return path
