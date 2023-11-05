import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLabel

class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Database Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 780, 580)
        self.tableWidget.mouseMoveEvent = self.onTableMouseMove  # Подключаем обработчик события mouseMoveEvent

        self.loadDatabaseData()

    def loadDatabaseData(self):
        try:
            # Подключаемся к базе данных
            connection = sqlite3.connect('db')
            cursor = connection.cursor()

            # Извлекаем данные из базы данных
            cursor.execute('SELECT * FROM name_of_olymp')
            data = cursor.fetchall()

            # Заголовки столбцов
            column_headers = [description[0] for description in cursor.description]
            self.tableWidget.setColumnCount(len(column_headers))
            self.tableWidget.setHorizontalHeaderLabels(column_headers)

            # Заполняем таблицу данными
            self.tableWidget.setRowCount(len(data))
            for row_num, row_data in enumerate(data):
                for col_num, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.tableWidget.setItem(row_num, col_num, item)

            connection.close()
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

    def onTableMouseMove(self, event):
        item = self.tableWidget.itemAt(event.pos())  # Получаем элемент таблицы, над которым находится мышь
        if item and item.column() == 0:  # Проверяем, что мышь находится над первым столбцом (где находится название базы данных)
            database_name = item.text()
            self.showDatabaseInfo(database_name)

    def showDatabaseInfo(self, database_name):
        dialog = QDialog(self)
        dialog.setWindowTitle('Database Info')
        dialog.setGeometry(200, 200, 400, 100)

        layout = QVBoxLayout()
        label = QLabel(f"Database Name: {database_name}")
        layout.addWidget(label)
        dialog.setLayout(layout)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DatabaseViewer()
    window.show()
    sys.exit(app.exec_())