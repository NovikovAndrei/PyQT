from PySide6 import QtWidgets
from newNote_form import Ui_FormNewNote
from notes_menu import WindowMenu
from animation import LoadScreen, HandleThread

class WindowNewNote(QtWidgets.QDialog):

    def __init__(self, parent=None, window_menu=None):
        super().__init__(parent)

        self.ui_newNote = Ui_FormNewNote()
        self.ui_newNote.setupUi(self)
        self.window_menu = window_menu

        self.ui_newNote.pushButtonSave.clicked.connect(self.saveNote)
        self.ui_newNote.pushButtonExit.clicked.connect(self.close)


    def saveNote(self):
        pass




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowNewNote()
    window.show()

    app.exec_()