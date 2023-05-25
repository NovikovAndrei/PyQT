import time

from PySide6 import QtCore, QtWidgets, QtGui

class LoadScreen(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

        # Таймер для вызова метода, для подгонки размера под родителя
        timer = QtCore.QTimer(self)
        timer.setInterval(10)
        timer.timeout.connect(lambda: self.resize(self.parent().size()))
        timer.start()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.hide()  # скрываем по умолчанию

        self.movie = QtGui.QMovie()


        labelAnimation = QtWidgets.QLabel()
        labelAnimation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        labelAnimation.setScaledContents(True)
        labelAnimation.setMovie(self.movie)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(labelAnimation)


        self.setLayout(layout)

    def startAnimation(self) -> None:
        """
        Запуск анимации

        :return: None
        """

        self.show()
        self.parent().setEnabled(False)
        self.movie.start()

    def stopAnimation(self) -> None:
        """
        Остановка анимации

        :return: None
        """

        self.hide()
        self.parent().setEnabled(True)
        self.movie.stop()


    def setGifPath(self, path: str) -> None:
        """
        Установка пути к GIF-файлу

        :param path: путь к GIF-файлу
        :return: None
        """
        self.movie.setFileName(path)



class HandleThread(QtCore.QThread):
    sending = QtCore.Signal(str)

    def __init__(self, delay=3):
        super().__init__()
        self.delay = delay

    def set_delay(self, delay):
        self.delay = delay

    def run(self):
        time.sleep(self.delay)


class SplashScreen(QtWidgets.QSplashScreen):
    """
    Создание класса на базе QSplashScreen для отключения события mousePressEvent
    """

    def mousePressEvent(self, arg__1: QtGui.QMouseEvent) -> None:
        pass


