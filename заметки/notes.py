from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from note_ui import Ui_Dialog
import sys


class NotesApp(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.add_note)
        self.deleteBtn.clicked.connect(self.delete_note)

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
