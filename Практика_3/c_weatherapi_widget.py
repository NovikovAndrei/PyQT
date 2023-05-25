"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
# """
import time
import requests
from PySide6 import QtWidgets, QtCore
from form_weather import Ui_FormWeather
from a_threads import WeatherHandler


class WindowWeather(QtWidgets.QWidget):
    lat = 36.826903
    lon = 10.173742

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_s = Ui_FormWeather()
        self.ui_s.setupUi(self)
        self.weatherHandler = WeatherHandler(WindowWeather.lat, WindowWeather.lon)
        self.initThreads()
        self.ui_s.radioButton3.setChecked(True)
        self.ui_s.radioButton3.clicked.connect(self.updateDelay)
        self.ui_s.radioButton5.clicked.connect(self.updateDelay)
        self.ui_s.radioButton10.clicked.connect(self.updateDelay)

        self.ui_s.pushButtonGetData.clicked.connect(self.getData)
        self.ui_s.pushButtonStopGetData.clicked.connect(self.stopGetData)

        self.ui_s.lineEditLatitude.setText("36.826903")
        self.ui_s.lineEditLongitude.setText("10.173742")

        self.ui_s.lineEditLatitude.textChanged.connect(self.validateLatitude)
        self.ui_s.lineEditLongitude.textChanged.connect(self.validateLongitude)

        self.ui_s.lineEditLatitude.textChanged.connect(self.stopGetDataUpdateCoord)
        self.ui_s.lineEditLongitude.textChanged.connect(self.stopGetDataUpdateCoord)


    def initThreads(self):
        self.weatherHandler.weatherInfoReceived.connect(self.upgradeWeatherInfo)

    def updateDelay(self):
        if self.ui_s.radioButton3.isChecked():
            self.weatherHandler.setDelay(3)
        elif self.ui_s.radioButton5.isChecked():
            self.weatherHandler.setDelay(5)
        elif self.ui_s.radioButton10.isChecked():
            self.weatherHandler.setDelay(10)

    def getData(self):
        WindowWeather.lat = float(self.ui_s.lineEditLatitude.text())
        WindowWeather.lon = float(self.ui_s.lineEditLongitude.text())
        self.weatherHandler.setCoordinates(WindowWeather.lat, WindowWeather.lon)  # Обновляем координаты в WeatherHandler
        self.weatherHandler.setStatus(True)
        self.ui_s.textEditData.clear()
        self.ui_s.pushButtonGetData.setEnabled(False)
        self.ui_s.pushButtonStopGetData.setEnabled(True)
        self.weatherHandler.start()

    def stopGetData(self):
        self.weatherHandler.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)

    def stopGetDataUpdateCoord(self):
        self.ui_s.textEditData.setText('<font color="red">Координаты изменены</font>')
        self.weatherHandler.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)

    def upgradeWeatherInfo(self, weather_data):
        temperature = weather_data['current_weather']['temperature']
        self.ui_s.textEditData.append(f"Температура: {temperature}°C")

    def validateLatitude(self):
        latitude_text = self.ui_s.lineEditLatitude.text()
        try:
            latitude = float(latitude_text)
            if -180 <= latitude <= 180:
                self.ui_s.lineEditLatitude.setStyleSheet("")
            else:
                self.ui_s.lineEditLatitude.setStyleSheet("background-color: red;")
                self.initErrorBox()


        except ValueError:
            self.ui_s.lineEditLatitude.setStyleSheet("background-color: red;")
            self.initErrorBox()


    def validateLongitude(self):
        longitude_text = self.ui_s.lineEditLongitude.text()
        try:
            longitude = float(longitude_text)
            if -180 <= longitude <= 180:
                self.ui_s.lineEditLongitude.setStyleSheet("")
            else:
                self.ui_s.lineEditLongitude.setStyleSheet("background-color: red;")
                self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
        except ValueError:
            self.ui_s.lineEditLongitude.setStyleSheet("background-color: red;")
            self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')

    def initErrorBox(self):
        error_box = QtWidgets.QMessageBox()
        error_box.setIcon(QtWidgets.QMessageBox.Warning)
        error_box.setWindowTitle("Ошибка")
        error_box.setText("Введите корректные координаты!")
        error_box.exec()



class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 3
        self.__status = None

    def setDelay(self, delay) -> None:
        self.__delay = delay

    def setCoordinates(self, lat, lon) -> None:
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    def setStatus(self, val):
        self.__status = val

    def run(self) -> None:
        while self.__status:
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherInfoReceived.emit(data)
            time.sleep(self.__delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()