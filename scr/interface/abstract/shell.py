from typing import Optional, Union

from PySide6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout

from scr.scripts.tools.file import FileLoader


class ShellFrame(QFrame):
    """
    Customizable frame for a shell interface.
    """

    def __init__(self, __parent = None, shell_layout_type: str = "vertical",
                 width: int = 600, height: int = 400):
        """
        Initializes the ShellFrame object with the specified parameters.

        Parameters:
        __parent (QWidget): Optional parameter for setting the parent widget.
        shell_layout_type (str): Specifies the layout type for the shell frame (default: "vertical").
        width (int): Width of the shell frame (default: 600).
        height (int): Height of the shell frame (default: 400).
        """

        super().__init__(__parent)

        if shell_layout_type == "vertical": self.mainLayout = QVBoxLayout()
        elif shell_layout_type == "horizontal": self.mainLayout = QHBoxLayout()

        self.setLayout(self.mainLayout)

        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        self.setStyleSheet(FileLoader.load_style("scr/interface/abstract/styles/shell.css"))
        self.setObjectName("shell")

    def add_widget(self, __widget, stretch: Optional[int] = None) -> None:
        """
        Adds a widget to the shell frame.

        Parameters:
        __widget (QWidget): The widget to be added.
        stretch (int): Optional parameter to specify stretching factor.
        """

        if stretch is not None:
            self.mainLayout.addWidget(__widget, stretch=stretch)
        else:
            self.mainLayout.addWidget(__widget)

    def add_layout(self, __layout) -> None:
        """
        Adds a layout to the shell frame.

        Parameters:
        __layout (QLayout): The layout to be added to the frame.
        """

        self.mainLayout.addLayout(__layout)