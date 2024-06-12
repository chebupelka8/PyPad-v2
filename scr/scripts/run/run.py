import os
import threading

from ..tools.file import FileChecker


class FileRunner:
    @staticmethod
    def run_python_file(__path: str, __dir: str) -> None:
        if not FileChecker.is_python_file(__path):
            return

        thread = threading.Thread(
            target=lambda: os.system(
                f"cd {os.path.normpath(__dir)} && python.exe {os.path.basename(os.path.normpath(__path))}"
            )
        )
        thread.start()
