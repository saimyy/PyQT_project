from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from a import Ui_MainWindow
from main import TableWidgetExample


class ProgramInfoWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, info_text):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Информация о программе")
        self.setGeometry(100, 100, 300, 350)
        self.setFixedSize(300, 350)
        self.tb1.setPlainText(info_text)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.info_text = None
        self.program_info_window = None
        self.program_info_window2 = None
        uic.loadUi('greeting.ui', self)
        self.setWindowTitle('Приветственное окно')
        self.about.clicked.connect(self.con_about)
        self.run.clicked.connect(self.run_proj)

    def con_about(self):
        if self.info_text is not None:
            if not self.program_info_window:
                self.program_info_window = ProgramInfoWindow(self.info_text)
            self.program_info_window.show()

    def run_proj(self):
        if not self.program_info_window2:
            self.program_info_window2 = TableWidgetExample()
        self.program_info_window2.show()

    def load_info_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.info_text = file.read()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.load_info_from_file("about.txt")
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
