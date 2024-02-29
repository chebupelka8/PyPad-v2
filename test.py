from PySide6.QtWidgets import QLabel, QApplication
from PySide6.QtGui import QColor

app = QApplication([])

label = QLabel()
text = "<span style='color: white;'>Белая часть</span><span style='color: yellow;'>Желтая часть</span>"
label.setText(text)
label.show()

app.exec_()