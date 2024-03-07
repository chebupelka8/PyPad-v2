"""PyPad - is a code editor for different programming languages.
PyPad supports some languages like a Python, Json, Html and CSS.
So far, PyPad is in development, and it is not suitable for use,
but you can watch the demo version of the project and test it."""

from .scripts.tools.file import FileDialog
from .scripts.run import FileRunner
from .widgets import *
from .exceptions import *
from .configs import *
from .subwidgets import *


INFO = """
version: v0.2.2-alpha
current build: pre-release
git-hub: https://github.com/chebupelka8/PyPad-v.2
"""

print("Welcome to PyPad!")
