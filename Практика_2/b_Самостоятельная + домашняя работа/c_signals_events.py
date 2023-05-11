"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtGui
from ui.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonMoveCoords.clicked.connect(self.moveOnCoord)
        self.ui.pushButtonLT.clicked.connect(self.moveLeftTop)
        self.ui.pushButtonRT.clicked.connect(self.moveRightTop)
        self.ui.pushButtonLB.clicked.connect(self.moveLeftBottom)
        self.ui.pushButtonRB.clicked.connect(self.moveRightBottom)
        self.ui.pushButtonCenter.clicked.connect(self.moveCenter)
        self.ui.pushButtonGetData.clicked.connect(self.currentTime)
        self.ui.pushButtonGetData.clicked.connect(self.screenCount)
        self.ui.pushButtonGetData.clicked.connect(self.currentWindow)
        self.ui.pushButtonGetData.clicked.connect(self.screenResolutinon)
        self.ui.pushButtonGetData.clicked.connect(self.currentScreen)
        self.ui.pushButtonGetData.clicked.connect(self.currentSizeWindow)
        self.ui.pushButtonGetData.clicked.connect(self.minSizeWindow)
        self.ui.pushButtonGetData.clicked.connect(self.currentCoordWindow)
        self.ui.pushButtonGetData.clicked.connect(self.centerCoordWindow)
        self.ui.pushButtonGetData.clicked.connect(self.currentStateWindow)

    # slots --------------------------------------------------------------

    def moveOnCoord(self):
        x = int(self.ui.spinBoxX.text())
        y = int(self.ui.spinBoxY.text())
        self.move(x, y)

    def moveLeftTop(self):
        self.move(0,0)

    def moveRightTop(self):
        self.move(1060,0)

    def moveLeftBottom(self):
        self.move(0,400)

    def moveRightBottom(self):
        self.move(1060,400)

    def moveCenter(self):
        self.move(500,200)

    def currentTime(self):
        self.ui.plainTextEdit.appendPlainText(f"Отчет сформирован: {time.ctime()}")

    def screenCount(self):
        self.ui.plainTextEdit.appendPlainText("screenCount")

    def screenCount(self):
        self.ui.plainTextEdit.appendPlainText("screenCount")

    def currentWindow(self):
        current_main_window = str(QtWidgets.QApplication.activeWindow())
        self.ui.plainTextEdit.appendPlainText(f"Текущее основное окно: {current_main_window}")

    def screenResolutinon(self):
        self.ui.plainTextEdit.appendPlainText("screenResolutinon")

    def currentScreen(self):
        self.ui.plainTextEdit.appendPlainText("currentScreen")

    def currentSizeWindow(self):
        self.ui.plainTextEdit.appendPlainText("Текущий размер окна: " + str(self.size()))

    def minSizeWindow(self):
        self.ui.plainTextEdit.appendPlainText("Минимальный размер окна: " + str(self.minimumSize()))

    def currentCoordWindow(self):
        self.ui.plainTextEdit.appendPlainText("Текущие координаты окна: " + str(self.pos()))

    def centerCoordWindow(self):
        centerX = self.pos().x() / 2
        centerY = self.pos().y() / 2
        self.ui.plainTextEdit.appendPlainText(f"Координаты центра приложения: ({centerX}, {centerY})")

    def currentStateWindow(self):
        winstate = str(self.windowState())
        state = []

        if winstate == "WindowState.WindowMaximized":
            state.append("развернуто на весь экран")
        elif winstate == "WindowState.WindowMinimized":
            state.append("свернуто")
        else:
            state.append("развернуто")

        if self.isActiveWindow():
            state.append("активно")
        if not self.isActiveWindow():
            state.append("неактивно")

        if self.isVisible():
            state.append("отображено")
        if not self.isVisible():
            state.append("скрыто")

        self.ui.plainTextEdit.appendPlainText(f"Состояние окна: {state}")



# events_____________________________________________

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(event.oldPos(), ">>>", event.pos(), time.ctime())

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print(event.size())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
