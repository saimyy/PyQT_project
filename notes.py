import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from note_ui import Ui_Dialog


class NoteApp(QMainWindow, Ui_Dialog):
    def __init__(self, name_bd):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.add_note)
        self.pushButton_2.clicked.connect(self.delete_note)
        self.load_notes(name_bd)
        self.db = name_bd
        self.setWindowTitle('Окно Заметок')

    def load_notes(self, name_bd):
        self.list_notes.clear()
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, content FROM {name_bd}")
        notes = cursor.fetchall()
        for note in notes:
            self.list_notes.addItem(f"{note[1]}")
        conn.close()

    def add_note(self):
        note_text = self.new_note.text()
        name_bd = self.db
        if note_text:
            conn = sqlite3.connect("notes.db")
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO {name_bd} (content) VALUES (?)", (note_text,))
            conn.commit()
            conn.close()
            self.load_notes(name_bd)
            self.new_note.clear()

    def delete_note(self):
        name_bd = self.db
        selected_item = self.list_notes.currentItem()
        if selected_item:
            note_id = selected_item.text()
            conn = sqlite3.connect("notes.db")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {name_bd} WHERE content=?", (note_id,))
            conn.commit()
            conn.close()
            self.load_notes(name_bd)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    note_app = NoteApp()
    note_app.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
