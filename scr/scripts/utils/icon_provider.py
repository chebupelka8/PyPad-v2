from PySide6.QtCore import QFileInfo
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileIconProvider

from scr.configs.pics import IconPaths


class IconProvider(QFileIconProvider):
    def icon(self, __info: QFileInfo):
        try:

            if __info.isDir():
                return QIcon(IconPaths.FolderIcons.DEFAULT)

            elif __info.isFile():
                if __info.suffix().lower() == "py":
                    return QIcon(IconPaths.FileIcons.PYTHON)

                elif __info.suffix().lower() in ("png", "jpg", "jpeg", "ico"):
                    return QIcon(IconPaths.FileIcons.PICTURE)

                elif __info.suffix().lower() in ("qss", "css"):
                    return QIcon(IconPaths.FileIcons.CSS)

                elif __info.suffix().lower() == "json":
                    return QIcon(IconPaths.FileIcons.JSON)

                elif __info.suffix().lower() == "txt":
                    return QIcon(IconPaths.FileIcons.TXT)

                elif __info.suffix().lower() == "java":
                    return QIcon(IconPaths.FileIcons.JAVA)

                elif __info.suffix().lower() == "html":
                    return QIcon(IconPaths.FileIcons.HTML)

                elif __info.suffix().lower() == "js":
                    return QIcon(IconPaths.FileIcons.JS)

                elif __info.suffix().lower() == "md":
                    return QIcon(IconPaths.FileIcons.README)

        except AttributeError:
            pass

        return super().icon(__info)
