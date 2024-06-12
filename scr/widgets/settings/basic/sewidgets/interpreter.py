from scr.interface.basic import PathEntry
from scr.scripts.tools.managers import InterpreterManager

from ...abstract import (AbstractSettingFrame, AbstractSettingsWidget,
                         FrameTitles)


class InterpreterSettingsWidget(AbstractSettingsWidget):
    def __init__(self) -> None:
        super().__init__()

        self.python_interpreter_path = AbstractSettingFrame(
            "Python Interpreter",
            "Points to the path of the python global interpreter"
        )
        self.interpreter_line_edit = self.python_interpreter_path.add_widget(
            PathEntry(InterpreterManager.get_python_interpreter_path())
        ).get_entry()

        self.interpreter_line_edit.textChanged.connect(lambda path: InterpreterManager.set_python_interpreter_path(path))

        self.update_values()

        self.add_widget(FrameTitles.title("Font Settings"))
        self.add_widget(self.python_interpreter_path)

    def update_values(self):
        self.interpreter_line_edit.setText(InterpreterManager.get_python_interpreter_path())
