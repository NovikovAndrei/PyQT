
import datetime, json
from PySide6 import QtWidgets, QtGui, QtCore
from notes_form import Ui_FormMenuNotes
from newNote_form import Ui_FormNewNote


class WindowMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_menu = Ui_FormMenuNotes()
        self.ui_menu.setupUi(self)

        self.ui_menu.pushButtonNewNote.clicked.connect(self.createNewNote)
        self.ui_menu.pushButtonDeleteNote.clicked.connect(self.deleteNote)
        self.ui_menu.pushButtonOpenNote.clicked.connect(self.openNote)

        # Загрузка заметок из файла при запуске
        self.loadNotes()

    def createNewNote(self):
        newNote = WindowNewNote(self)
        newNote.saveNote.connect(self.addNewItem)
        newNote.exec()

    def addNewItem(self, note):
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setText(0, note[0])
        new_item.setText(1, note[2])
        new_item.setText(2, note[3])
        new_item.setText(3, note[4])
        new_item.setText(5, note[1])
        if note[4] == "Выполнено":
            new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        elif note[4] == "Не выполнено":
            new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(255, 0, 0)))

        # Добавляем элемент в QTreeWidget
        self.ui_menu.treeWidgetNotes.addTopLevelItem(new_item)

        # Сохраняем заметку в файл
        self.saveNotes()

    def saveNotes(self):
        notes = []

        # Собираем все заметки из QTreeWidget
        for index in range(self.ui_menu.treeWidgetNotes.topLevelItemCount()):
            item = self.ui_menu.treeWidgetNotes.topLevelItem(index)
            header = item.text(0)
            note = item.text(5)
            creation_date = item.text(1)
            deadline = item.text(2)
            status = item.text(3)
            notes.append({
                "header": header,
                "note": note,
                "creation_date": creation_date,
                "deadline": deadline,
                "status": status
            })

        # Сохраняем заметки в файле notes.json
        with open("notes.json", "w") as file:
            json.dump(notes, file)

    def loadNotes(self):
        try:
            # Load notes from the "notes.json" file
            with open("notes.json", "r") as file:
                notes = json.load(file)

            # Add notes to QTreeWidget
            for note in notes:
                new_item = QtWidgets.QTreeWidgetItem()
                new_item.setText(0, note["header"])
                new_item.setText(1, note["creation_date"])
                new_item.setText(2, note["deadline"])
                new_item.setText(3, note["status"])
                new_item.setText(5, note["note"])
                if note["status"] == "Выполнено":
                    new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(0, 255, 0)))
                elif note["status"] == "Не выполнено":
                    new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(255, 0, 0)))

                # Add the new item to QTreeWidget
                self.ui_menu.treeWidgetNotes.addTopLevelItem(new_item)

        except FileNotFoundError:
            # Если файл "notes.json" не существует
            pass

    def deleteNote(self):
        selected_items = self.ui_menu.treeWidgetNotes.selectedItems()
        if not selected_items:
            error_box = QtWidgets.QMessageBox()
            error_box.setIcon(QtWidgets.QMessageBox.Warning)
            error_box.setWindowTitle("Ошибка")
            error_box.setText("Выберите заметку для удаления!")
            error_box.exec()
            return
        confirm_box = QtWidgets.QMessageBox()
        confirm_box.setIcon(QtWidgets.QMessageBox.Question)
        confirm_box.setWindowTitle("Подтверждение удаления")
        confirm_box.setText("Вы действительно хотите удалить выбранную заметку?")
        confirm_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        confirm_box.setDefaultButton(QtWidgets.QMessageBox.No)
        confirm_box.button(QtWidgets.QMessageBox.Yes).setText("Да")
        confirm_box.button(QtWidgets.QMessageBox.No).setText("Нет")
        confirm_result = confirm_box.exec()

        if confirm_result == QtWidgets.QMessageBox.Yes:
            for item in selected_items:
                index = self.ui_menu.treeWidgetNotes.indexOfTopLevelItem(item)
                self.ui_menu.treeWidgetNotes.takeTopLevelItem(index)
        # Сохраните заметки после удаления
        self.saveNotes()

    def openNote(self):
        selected_items = self.ui_menu.treeWidgetNotes.selectedItems()
        if not selected_items:
            error_box = QtWidgets.QMessageBox()
            error_box.setIcon(QtWidgets.QMessageBox.Warning)
            error_box.setWindowTitle("Ошибка")
            error_box.setText("Выберите заметку для открытия!")
            error_box.exec()
            return

        # Получение выбранного элемента
        selected_item = selected_items[0]

        # Извлечение данных заметки
        header = selected_item.text(0)
        note = selected_item.text(5)
        creation_date = selected_item.text(1)
        deadline = selected_item.text(2)
        status = selected_item.text(3)

        # Здесь вы можете выполнить дополнительные действия
        # для открытия заметки, например, создать новое окно и передать данные

        # Пример создания нового окна и передачи данных
        note_window = QtWidgets.QMessageBox()
        note_window.setIcon(QtWidgets.QMessageBox.Information)
        note_window.setWindowTitle("Открыть заметку")
        note_window.setText(f"Заголовок: {header}\n"
                            f"Заметка: {note}\n"
                            f"Дата создания: {creation_date}\n"
                            f"Срок выполнения: {deadline}\n"
                            f"Статус: {status}")
        note_window.exec()

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
        if len(self.ui_newNote.plainTextEditNote.toPlainText()) > 20:
            note_text = f"{self.ui_newNote.plainTextEditNote.toPlainText()[:20]}..."
        else:
            note_text = self.ui_newNote.plainTextEditNote.toPlainText()[:20]
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
            self.ui_newNote.plainTextEditNote.clear()
            self.ui_newNote.lineEditHeader.clear()
            self.ui_newNote.dateTimeEditDeadline.setDateTime(datetime.datetime.now())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = WindowMenu()
    window.show()

    app.exec()
