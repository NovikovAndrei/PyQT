import time
from PySide6 import QtWidgets, QtGui, QtCore
from notes_form import Ui_FormMenuNotes
from newNote_form import Ui_FormNewNote


class WindowMenu(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_menu = Ui_FormMenuNotes()
        self.ui_menu.setupUi(self)


        self.ui_menu.pushButtonNewNote.clicked.connect(self.createNote)



    def createNote(self):
        newNote = WindowNewNote()
        newNote.exec()
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setText(0, "New Item")

        # Добавляем элемент в QTreeWidget
        self.ui_menu.treeWidgetNotes.addTopLevelItem(new_item)






class WindowNewNote(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_newNote = Ui_FormNewNote()
        self.ui_newNote.setupUi(self)


        self.ui_newNote.pushButtonSave.clicked.connect(self.saveNote)
        self.ui_newNote.pushButtonExit.clicked.connect(self.close)


    def saveNote(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowMenu()
    window.show()

    app.exec()