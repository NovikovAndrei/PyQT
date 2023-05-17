"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from b_systeminfo_widget import WindowSystem
from c_weatherapi_widget import WindowWeather


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.windowWeather = WindowWeather()
        self.windowSystem = WindowSystem()

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.windowSystem)
        layout.addWidget(self.windowWeather)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()