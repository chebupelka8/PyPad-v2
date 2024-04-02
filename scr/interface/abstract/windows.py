from PySide6.QtWidgets import QDialog, QHBoxLayout
from PySide6.QtCore import Qt, QSize

from scr.scripts.tools.file import FileLoader
from .shell import ShellFrame

from typing import Optional


class DialogWindow(QDialog):
    """
    Customizable dialog window with frameless and keyboard inclusion settings.
    """

    def __init__(self, __parent,
                 width: int = 600, height: int = 400, *,
                 frameless: bool = True, keyboard_include: bool = True) -> None:
        """
        Initializes the DialogWindow object with the specified parameters.

        Parameters:
        __parent (QWidget): Parent widget for the dialog window.
        width (int): Width of the dialog window (default: 600).
        height (int): Height of the dialog window (default: 400).
        frameless (bool): Flag to determine if the window should be frameless (default: True).
        keyboard_include (bool): Flag to include keyboard shortcuts (default: True).
        """

        if frameless: super().__init__(__parent, f=Qt.WindowType.FramelessWindowHint)
        else: super().__init__(__parent)

        self.setMinimumSize(QSize(width, height))

        self.__keyboard_include = keyboard_include

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/dialog.css"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

    def keyPressEvent(self, event):
        if self.__keyboard_include:
            if event.key() == Qt.Key.Key_Return:
                self.accept()

            elif event.key() == Qt.Key.Key_Escape:
                self.reject()

            else:
                super().keyPressEvent(event)

        else:
            super().keyPressEvent(event)


class TransparentDialogWindow(DialogWindow):
    """
    Transparent dialog window with a shell frame.
    """

    def __init__(self, __parent, shell_layout_type: str = "vertical",
                 width: int = 600, height: int = 400, *,
                 frameless: bool = True) -> None:
        """
        Initializes the TransparentDialogWindow object with the specified parameters.

        Parameters:
        __parent (QWidget): Parent widget for the dialog window.
        shell_layout_type (str): Specifies the layout type for the shell frame (default: "vertical").
        width (int): Width of the dialog window (default: 600).
        height (int): Height of the dialog window (default: 400).
        frameless (bool): Flag to determine if the window should be frameless (default: True).
        """

        super().__init__(__parent, width, height, frameless=frameless)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shell = ShellFrame(self, shell_layout_type)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.shell)
        self.setLayout(self.mainLayout)

    def add_widget(self, widget, stretch: Optional[int] = None) -> None:
        """
        Adds a widget to the shell frame within the dialog window.
        """

        self.shell.add_widget(widget, stretch)

    def add_layout(self, layout) -> None:
        """
        Adds a layout to the shell frame within the dialog window.
        """

        self.shell.add_layout(layout)

    def set_shell(self, __shell: ShellFrame) -> None:
        """
        Sets a custom shell frame for the dialog window.
        """

        self.shell = __shell
