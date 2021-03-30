import os
import shutil
import sys
from datetime import datetime
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.check_path())
        # Обратите внимание: имя элемента такое же как в QTDesigner

        # self.label.setText("OK")
        # Имя элемента совпадает с objectName в QTDesigner

    def check_path(self):
        path_first = self.lineEdit.text()
        path_second = self.lineEdit.text()
        if not path_first and not path_second:
            self.label_3.setText("Пути не введены!")
            return
        else:
            if not os.path.exists(path_first) and not os.path.exists(path_second):
                self.label_3.setText("Пути введены некорректно")
                return
            else:
                dt_now = datetime.now()
                new_date = f"Archive {dt_now.year}-{dt_now.month}-{dt_now.day} {dt_now.hour}:{dt_now.minute}:{dt_now.second}"
                shutil.make_archive(new_date, 'zip', root_dir=path_first)
                path_new = "/".join(path_first.split('/')[:-1])
                shutil.move(path_new, path_second)
                self.label_3.setText("Успешно!")
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
