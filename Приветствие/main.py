import sys
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QTabWidget, QMainWindow, QPushButton, \
    QTableWidget, QTableWidgetItem
from olymp import OlympicsInfoWidget


class TableWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_data_from_database()
        self.res = None

    def initUI(self):
        self.setWindowTitle('Главное окно')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.central_widget.setLayout(self.layout)

    def load_data_from_database(self):
        connection = sqlite3.connect('db')
        cursor = connection.cursor()
        cursor.execute('SELECT name, date FROM main_window')

        data = cursor.fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(3)
        for row_num, (id, name) in enumerate(data):
            id_item = QTableWidgetItem(str(id))
            name_item = QTableWidgetItem(name)
            button = QPushButton('Подробнее')

            self.tableWidget.setItem(row_num, 0, id_item)
            self.tableWidget.setItem(row_num, 1, name_item)
            self.tableWidget.setCellWidget(row_num, 2, button)

            button.clicked.connect(self.button_clicked)

        column_names = ['Name', 'Date', 'About']
        self.tableWidget.setHorizontalHeaderLabels(column_names)

    def button_clicked(self):
        button = self.sender()
        if isinstance(button, QPushButton):
            row = self.tableWidget.indexAt(button.pos()).row()
            id = self.tableWidget.item(row, 0).text()
            if id == 'Высшая проба':
                if not self.res:
                    self.res = OlympicsInfoWidget('Высшая проба', 'vshe')
                self.res.show()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableWidgetExample()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
