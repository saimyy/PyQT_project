from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from note_ui import Ui_Dialog

class NotesApp(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.add_note)
        self.pushButton_2.clicked.connect(self.delete_note)

    def add_note(self):
        note_text = self.new_note.text()
        self.list_notes.addItem(note_text)
        self.new_note.setText('')

    def delete_note(self):
        selected_note = self.list_notes.currentRow()
        if selected_note != -1:
            self.list_notes.takeItem(selected_note)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes_app = NotesApp()
    notes_app.show()
    sys.exit(app.exec_())
