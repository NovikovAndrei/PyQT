import datetime
import json
import time

from PySide6 import QtWidgets, QtGui, QtCore
from notes_form import Ui_FormMenuNotes
from newNote_form import Ui_FormNewNote
from animation import LoadScreen, HandleThread, SplashScreen

class WindowMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_menu = Ui_FormMenuNotes()
        self.ui_menu.setupUi(self)
        self.loadGUI()
        self.setStyleSheet("""
            WindowMenu {
                background-color: #eef2f5; 
            }
        """)
        self.ui_menu.treeWidgetNotes.setStyleSheet("background-color: #eef2f5;")
        self.load_screen = LoadScreen(self)
        self.load_screen.setGifPath("images/boom.gif")
        self.handleThread = HandleThread()
        self.handleThread.set_delay(2)
        self.handleThread.started.connect(self.load_screen.startAnimation)
        self.handleThread.finished.connect(self.load_screen.stopAnimation)
        # Устанавка ширины столбцов
        self.ui_menu.treeWidgetNotes.setColumnWidth(0, 200)
        self.ui_menu.treeWidgetNotes.setColumnWidth(1, 150)
        self.ui_menu.treeWidgetNotes.setColumnWidth(2, 150)
        self.ui_menu.treeWidgetNotes.setColumnWidth(3, 150)

        self.ui_menu.pushButtonNewNote.clicked.connect(self.createNewNote)
        self.ui_menu.pushButtonDeleteNote.clicked.connect(self.deleteNote)
        self.ui_menu.pushButtonOpenNote.clicked.connect(self.openNote)
        self.ui_menu.treeWidgetNotes.itemDoubleClicked.connect(self.openNoteDoubleClick)
        self.ui_menu.pushButtonEditNote.clicked.connect(self.editNote)
        self.loadNotes()

    def createNewNote(self) -> None:
        """
        Открытие окна создания новой заметки
        :return: None
        """
        newNote = WindowNewNote(self)
        newNote.saveNote.connect(self.addNewItem)
        newNote.exec()

    def addNewItem(self, note: list) -> None:
        """
        Добавление новой заметки
        """
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setText(0, note[0])
        new_item.setText(1, note[2])
        new_item.setText(2, note[3])
        new_item.setText(3, note[4])
        new_item.setText(4, note[1])
        if note[4] == "Выполнено":
            new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        elif note[4] == "Не выполнено":
            new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(255, 0, 0)))

        # Добавляем элемент в QTreeWidget
        self.ui_menu.treeWidgetNotes.addTopLevelItem(new_item)

        # Сохраняем заметку в файл
        self.saveNotes()

    def saveNotes(self) -> None:
        """
        Сохранение заметки
        """
        notes = []

        # Собираем все заметки из QTreeWidget
        for index in range(self.ui_menu.treeWidgetNotes.topLevelItemCount()):
            item = self.ui_menu.treeWidgetNotes.topLevelItem(index)
            header = item.text(0)
            note = item.text(4)
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

    def loadNotes(self) -> None:
        """
        Загрузка заметок
        """
        try:
            with open("notes.json", "r") as file:
                notes = json.load(file)

            # Добавляем в QTreeWidget
            for note in notes:
                new_item = QtWidgets.QTreeWidgetItem()
                new_item.setText(0, note["header"])
                new_item.setText(1, note["creation_date"])
                new_item.setText(2, note["deadline"])
                new_item.setText(3, note["status"])
                new_item.setText(4, note["note"])
                if note["status"] == "Выполнено":
                    new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(0, 255, 0)))
                elif note["status"] == "Не выполнено":
                    new_item.setBackground(3, QtGui.QBrush(QtGui.QColor(255, 0, 0)))

                # Add the new item to QTreeWidget
                self.ui_menu.treeWidgetNotes.addTopLevelItem(new_item)

        except FileNotFoundError:
            # файл "notes.json" не существует
            pass

    def deleteNote(self) -> None:
        """
        Удаление заметки
        """
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
        self.saveNotes()
        # запуск анимации
        self.handleThread.start()

    def openNote(self) -> None:
        """
        Открытие заметки
        """
        selected_items = self.ui_menu.treeWidgetNotes.selectedItems()
        # если заметка не выбрана
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
        note = selected_item.text(4)
        creation_date = selected_item.text(1)
        deadline = selected_item.text(2)
        status = selected_item.text(3)

        # показ заметки
        note_window = QtWidgets.QMessageBox()
        note_window.setIcon(QtWidgets.QMessageBox.Information)
        note_window.setWindowTitle(header)
        note_window.setText(
                            f"{note}\n"
                            f"Дата создания: {creation_date}\n"
                            f"Срок выполнения: {deadline}\n"
                            f"Статус: {status}")
        note_window.exec()

    def openNoteDoubleClick(self) -> None:
        """Открытие заметки двойным кликом"""
        self.openNote()


    def editNote(self) -> None:
        """Редактирование заметки"""
        selected_items = self.ui_menu.treeWidgetNotes.selectedItems()
        # если не выбрана заметка для ркдактирования
        if not selected_items:
            error_box = QtWidgets.QMessageBox()
            error_box.setIcon(QtWidgets.QMessageBox.Warning)
            error_box.setWindowTitle("Ошибка")
            error_box.setText("Выберите заметку для редактирования!")
            error_box.exec()
            return

        # Получение выбранного элемента
        selected_item = selected_items[0]

        # Получение индекса выбранного элемента
        index = self.ui_menu.treeWidgetNotes.indexOfTopLevelItem(selected_item)

        # Извлечение данных заметки
        header = selected_item.text(0)
        note = selected_item.text(4)
        deadline = selected_item.text(2)
        status = selected_item.text(3)

        # Создание окна редактирования заметки
        edit_note_window = WindowNewNote(self)
        edit_note_window.ui_newNote.lineEditHeader.setText(header)
        edit_note_window.ui_newNote.plainTextEditNote.setPlainText(note)
        edit_note_window.ui_newNote.dateTimeEditDeadline.setDateTime(
            datetime.datetime.strptime(deadline, "%d.%m.%Y %H:%M"))
        if status == "Выполнено":
            edit_note_window.ui_newNote.radioButtonDone.setChecked(True)
        else:
            edit_note_window.ui_newNote.radioButtonNotDone.setChecked(True)

        # Обновление заметки после редактирования
        edit_note_window.saveNote.connect(lambda note: self.updateNoteItem(index, note))
        edit_note_window.exec()

    def updateNoteItem(self, index, note) -> None:
        """Обновление заметок"""
        item = self.ui_menu.treeWidgetNotes.topLevelItem(index)
        item.setText(0, note[0]) #header_text
        item.setText(4, note[1]) #note_text
        item.setText(3, note[4]) #status
        item.setText(2, note[3]) #deadline_text
        if note[4] == "Выполнено":
            item.setBackground(3, QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        elif note[4] == "Не выполнено":
            item.setBackground(3, QtGui.QBrush(QtGui.QColor(255, 0, 0)))
        print(note)
        # Сохранение заметок после обновления

        self.saveNotes()

    def loadGUI(self):
        """
        'Долгая' загрузка приложения

        """

        splash = SplashScreen(QtGui.QPixmap("images/start3.png"))

        splash.showMessage("Загрузка данных...     0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
        splash.show()
        for _ in range(100):
            time.sleep(0.005)
            if (_ % 10) == 0:
                splash.showMessage(f"Загрузка данных...     {_}%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter, QtCore.Qt.black)

        splash.finish(self)
        self.show()

class WindowNewNote(QtWidgets.QDialog):
    saveNote = QtCore.Signal(list)  # Определение сигнала

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_newNote = Ui_FormNewNote()
        self.ui_newNote.setupUi(self)
        self.setStyleSheet("""
            WindowNewNote {
                background-color: #eef2f5; 
            }
        """)
        self.load_screen = LoadScreen(self)
        self.load_screen.setGifPath("images/cat.gif")
        self.handleThread = HandleThread()
        self.handleThread.started.connect(self.load_screen.startAnimation)
        self.handleThread.finished.connect(self.load_screen.stopAnimation)
        self.ui_newNote.dateTimeEditDeadline.setDateTime(datetime.datetime.now())
        self.ui_newNote.pushButtonSave.clicked.connect(self.ButtonSaveNote)
        self.ui_newNote.pushButtonExit.clicked.connect(self.close)


    def ButtonSaveNote(self) -> None:
        """Сохранение заметки при нажатии кнопки"""
        header_text = self.ui_newNote.lineEditHeader.text()
        note_text = self.ui_newNote.plainTextEditNote.toPlainText()
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
            self.handleThread.start()
            self.saveNote.emit([header_text, note_text, creationDate, deadline_text, status])
            self.ui_newNote.plainTextEditNote.clear()
            self.ui_newNote.lineEditHeader.clear()
            self.ui_newNote.dateTimeEditDeadline.setDateTime(datetime.datetime.now())





if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = WindowMenu()
    window.show()

    app.exec()
