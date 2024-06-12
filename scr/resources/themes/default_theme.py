from .abstract_theme import AbstractTheme


class TextEditorTheme(AbstractTheme):
    theme = AbstractTheme.theme["text-editor-theme"]

    DEFAULT = theme["default"]
