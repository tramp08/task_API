import sys

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import requests

class MyWidget(QMainWindow):
    def __init__(self, *argvs, **kwargs):
        super().__init__( *argvs, **kwargs)
        uic.loadUi('main_window.ui', self)  # Загружаем дизайн
        self.zoom = 12
        self.ll = [44.269759, 46.307743]
        self.api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
        self.show_map()

    def show_map(self):
        api_server = "https://static-maps.yandex.ru/v1"
        map_params = {
            'll':       ','.join(map(str, self.ll)),
            'z':        self.zoom,
            'apikey':    self.api_key
        }

        response = requests.get(api_server, params=map_params)
        if not response:
            print("Ошибка выполнения запроса:")
            print(response.url)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        map_image = QImage.fromData(response.content)
        pixmap = QPixmap.fromImage(map_image)
        self.g_map.setPixmap(pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())