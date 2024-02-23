from scr.scripts import FileLoader

from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter


class ImageViewer(QGraphicsView):
    def __init__(self, __path: str) -> None:
        super().__init__()

        self.__path = __path

        self.setStyleSheet(FileLoader.load_style("scr/widgets/styles/image_viewer.css"))
        self.setObjectName("image-viewer")

        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.ScrollHandDrag)

        self.pixmap = QPixmap(__path)
        self.scene().addPixmap(self.pixmap)

    def get_full_path(self) -> str:
        return self.__path

    def wheelEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            factor = 1.2

            if event.angleDelta().y() < 0:
                factor = 1.0 / factor

            self.scale(factor, factor)
        else:
            super().wheelEvent(event)
