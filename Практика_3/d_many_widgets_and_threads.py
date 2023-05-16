"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from form_system import Ui_FormSystem
from form_weather import Ui_FormWeather


class Window1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_s = Ui_FormSystem()
        self.ui_s.setupUi(self)

        self.ui_w = Ui_FormWeather()
        self.ui_w.setupUi(self)

        widget_s = QtWidgets.QWidget()
        self.ui_s.setupUi(widget_s)

        widget_w = QtWidgets.QWidget()
        self.ui_w.setupUi(widget_w)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget_s)
        layout.addWidget(widget_w)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.setMinimumSize(400, 400)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window1()
    window.show()

    app.exec()