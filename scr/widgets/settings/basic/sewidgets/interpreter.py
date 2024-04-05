from ...abstract import AbstractSettingsWidget, AbstractSettingFrame, FrameTitles

from scr.scripts.tools.managers import InterpreterManager


class InterpreterSettingsWidget(AbstractSettingsWidget):
    def __init__(self) -> None:
        super().__init__()

        self.python_interpreter_path = AbstractSettingFrame("Python Interpreter", "Points to the path of the python global interpreter")
        self.interpreter_line_edit = self.python_interpreter_path.add_path_entry(InterpreterManager.get_python_interpreter_path())
        self.interpreter_line_edit.textChanged.connect(lambda path: InterpreterManager.set_python_interpreter_path(path))

        self.update_values()

        self.mainLayout.addWidget(FrameTitles.title("Font Settings"))
        self.mainLayout.addWidget(self.python_interpreter_path)

    def update_values(self):
        self.interpreter_line_edit.setText(InterpreterManager.get_python_interpreter_path())
