import os

from PySide6.QtWidgets import QFileDialog


class FileDialog:
    @staticmethod
    def get_open_file_name():
        """
        Opens a file dialog to select a file and returns the file path.

        Returns:
        str: The selected file path or None if the file does not exist.
        """

        path = QFileDialog.getOpenFileName()[0]

        if not os.path.exists(path):
            print("Warning: {File not found}")
            return

        return path

    @staticmethod
    def get_open_directory():
        """
        Opens a directory dialog to select a directory and returns the directory path.

        Returns:
        str: The selected directory path or None if the directory does not exist.
        """

        path = QFileDialog.getExistingDirectory()

        if not os.path.exists(path):
            print("Warning: {Directory not found}")
            return

        return path
