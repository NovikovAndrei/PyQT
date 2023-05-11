"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore
from ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(["oct", "hex", "bin", "dec"])

        self.settings = QtCore.QSettings("d_eventfilter_settings", "MyApp")
        self.ui.comboBox.setCurrentIndex(self.settings.value("display_mode", 0))
        self.ui.lcdNumber.display(self.settings.value("lcd_value", 0))
        self.ui.dial.setValue(self.settings.value("dial_value", 0))
        self.ui.horizontalSlider.setValue(self.settings.value("horizontalSlider_value", 0))

        self.ui.dial.installEventFilter(self)
        self.ui.dial.valueChanged.connect(self.valueChanged)
        self.ui.horizontalSlider.valueChanged.connect(self.valueChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.changeFormat)


    #slot_____________________________

    def changeFormat(self, index):
        value = self.ui.lcdNumber.value()
        if index == 0:  # oct
            self.ui.lcdNumber.setOctMode()
        elif index == 1:  # hex
            self.ui.lcdNumber.setHexMode()
        elif index == 2:  # bin
            self.ui.lcdNumber.setBinMode()
        elif index == 3:  # dec
            self.ui.lcdNumber.setDecMode()
        self.ui.lcdNumber.display(value)

    def valueChanged(self, value):
        self.ui.lcdNumber.display(value)
        self.ui.horizontalSlider.setValue(value)
        self.ui.dial.setValue(value)


    # events__________________________

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.ui.dial and event.type() == QtCore.QEvent.Type.KeyPress:
            if event.key() == QtCore.Qt.Key.Key_Plus:
                value = self.ui.dial.value() + 1
                self.ui.dial.setValue(value)
                print(value)

            if event.key() == QtCore.Qt.Key.Key_Minus:
                value = self.ui.dial.value() - 1
                if value < 0:
                    value = 0
                self.ui.dial.setValue(value)
                print(value)

        return super(Window, self).eventFilter(watched, event)

    def closeEvent(self, event):
        self.settings.setValue("display_mode", self.ui.comboBox.currentIndex())
        self.settings.setValue("lcd_value", self.ui.lcdNumber.value())
        self.settings.setValue("dial_value", self.ui.dial.value())
        self.settings.setValue("horizontalSlider_value", self.ui.horizontalSlider.value())
        super(Window, self).closeEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
