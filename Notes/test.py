
import time, datetime
from PySide6 import QtWidgets, QtGui, QtCore
from notes_form import Ui_FormMenuNotes
from newNote_form import Ui_FormNewNote


class WindowMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_menu = Ui_FormMenuNotes()
        self.ui_menu.setupUi(self)

        self.ui_menu.pushButtonNewNote.clicked.connect(self.createNewNote)

    def createNewNote(self):
        newNote = WindowNewNote(self)
        newNote.saveNote.connect(self.addNewItem)
        newNote.exec()

    def addNewItem(self, note):
        redBackground = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        greenBackground = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setText(0, note[0])
        new_item.setText(1, note[2])
        new_item.setText(2, note[3])
        new_item.setText(3, note[4])
        new_item.setText(5, note[1])
        if note[4] == "Выполнено":
            new_item.setBackground(3, greenBackground)
        else:
            new_item.setBackground(3, redBackground)




        # Добавляем элемент в QTreeWidget
        self.ui_menu.treeWidgetNotes.addTopLevelItem(new_item)


class WindowNewNote(QtWidgets.QDialog):
    saveNote = QtCore.Signal(list)  # Определение сигнала

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_newNote = Ui_FormNewNote()
        self.ui_newNote.setupUi(self)
        self.ui_newNote.dateTimeEditDeadline.setDateTime(datetime.datetime.now())

        self.ui_newNote.pushButtonSave.clicked.connect(self.handleSave)
        self.ui_newNote.pushButtonExit.clicked.connect(self.close)

    def handleSave(self):
        header_text = self.ui_newNote.lineEditHeader.text()
        note_text = f"{self.ui_newNote.plainTextEditNote.toPlainText()[:20]}..."
        creationDate = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        deadline_text = self.ui_newNote.dateTimeEditDeadline.text()
        if self.ui_newNote.radioButtonDone.isChecked():
            status = "Выполнено"
        else:
            status = "Не выполнено"
        if note_text == "..." or header_text == "" or datetime.datetime.strptime(deadline_text, "%d.%m.%Y %H:%M") <= datetime.datetime.now():
            # Создание всплывающего окна ошибки
            error_box = QtWidgets.QMessageBox()
            error_box.setIcon(QtWidgets.QMessageBox.Warning)
            error_box.setWindowTitle("Ошибка")
            if note_text == "...":
                error_box.setText("Пустую заметку добавлять нельзя!")
            elif header_text == "":
                error_box.setText("Добавьте заголовок заметки!")
            elif datetime.datetime.strptime(deadline_text, "%d.%m.%Y %H:%M") <= datetime.datetime.now():
                error_box.setText("Срок выполнения не может быть раньше текущей даты!")
            error_box.exec()
        else:
            self.saveNote.emit([header_text, note_text, creationDate, deadline_text, status])


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = WindowMenu()
    window.show()

    app.exec()
