"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from form_system import Ui_FormSystem
from a_threads import SystemInfo


class WindowSystem(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_s = Ui_FormSystem()
        self.ui_s.setupUi(self)
        self.initThreads()

        self.ui_s.horizontalSlider.valueChanged.connect(self.valueChanged)

    def initThreads(self):
        self.SystemInfo = SystemInfo()
        self.SystemInfo.start()
        self.SystemInfo.systemInfoReceived.connect(self.updateProgressBarCPURAM)

    def updateProgressBarCPURAM(self, info):
        cpu_value, ram_value = info
        self.ui_s.progressBarCPU.setValue(cpu_value)
        self.ui_s.progressBarRAM.setValue(ram_value)

    def valueChanged(self, value):
        self.ui_s.lcdNumber.display(value)
        self.SystemInfo.delay = value


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowSystem()
    window.show()

    app.exec()
