"""PyPad - is a code editor for different programming languages.
PyPad supports some languages like a Python, Json, Html and CSS.
So far, PyPad is in development, and it is not suitable for use,
but you can watch the demo version of the project and test it."""

from .configs import *
from .exceptions import *
from .interface.additional import *
from .scripts.run import FileRunner
from .scripts.settings import *
from .scripts.theme import *
from .scripts.tools.file import FileDialog
from .subwidgets import *
from .widgets import *
from .widgets.settings import *

print(VersionConfig.__repr__())
