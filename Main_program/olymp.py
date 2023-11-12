import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from u import Ui_MainWindow
from Main_program.notes import NoteApp


class OlympicsInfoWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, name_olymp, name_bd):
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect('db')
        self.cursor = self.conn.cursor()
        self.refresh_info(name_olymp)
        self.db = name_bd
        self.pushButton.clicked.connect(self.do_note)
        self.res = None

    def do_note(self):
        bd = self.db
        if not self.res:
            self.res = NoteApp(bd)
        self.res.show()

    def refresh_info(self, name_ol):
        data = self.cursor.execute('SELECT description FROM name_of_olymp WHERE name = ?', (name_ol,)).fetchall()
        for row in data:
            self.textBrowser.append(row[0])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OlympicsInfoWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
