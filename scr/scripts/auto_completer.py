from jedi import Script
from PySide6.QtCore import QRunnable, QObject, Slot, Signal


class CompleterSignal(QObject):
    res = Signal(list)


class AutoCompleter(QRunnable):
    def __init__(self, __path: str, __text: str, __line: int, __column: int) -> None:
        super().__init__()

        self.__path = __path
        self.__text = __text
        self.__line = __line
        self.__column = __column
        self.__script = None
        self.signal = CompleterSignal()

        self.__completions = []

    def get_completions(self, __text: str, __line: int, __column: int) -> list[str] | None:
        if __text.strip("\n").strip(" ") == "": return
        self.__text = __text

        try:
            self.__script = Script(__text, path=self.__path)
            completions = self.__script.complete(__line, __column)

            res = [i.name for i in completions]

            return res

        except Exception as e:
            ...

    def get(self):
        return self.__completions

    def set_values(self, __text: str, __line: int, __column):
        self.__text = __text
        self.__line = __line
        self.__column = __column

    @Slot()
    def run(self):
        self.__completions = self.get_completions(self.__text, self.__line, self.__column)
        self.signal.res.emit(self.__completions)
