import os


class Path:
    @staticmethod
    def to_relative_path(
        __dir: str, __file: str, save_project_name: bool = True
    ) -> str:
        __dir = os.path.normpath(__dir)
        __file = os.path.normpath(__file)

        if save_project_name:
            __dir = "\\".join(__dir.split("\\")[:-1])
            index = __file.find(__dir)

            if index == -1:
                return __file

            path = __file[__file.find(__dir) + len(__dir) + 1 :]

            return path

        else:
            return __file[__file.find(__dir)]
