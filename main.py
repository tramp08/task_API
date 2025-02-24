import sys

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import requests

class MyWidget(QMainWindow):
    def __init__(self, *argvs, **kwargs):
        super().__init__( *argvs, **kwargs)
        uic.loadUi('main_window.ui', self)  # Загружаем дизайн


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())