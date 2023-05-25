# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_system.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QProgressBar, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_FormSystem(object):
    def setupUi(self, FormSystem):
        if not FormSystem.objectName():
            FormSystem.setObjectName(u"FormSystem")
        FormSystem.resize(700, 170)
        FormSystem.setMinimumSize(QSize(700, 170))
        FormSystem.setMaximumSize(QSize(16777215, 170))
        self.verticalLayout = QVBoxLayout(FormSystem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.label = QLabel(FormSystem)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(135, 0))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSlider = QSlider(FormSystem)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(16777215, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)

        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.lcdNumber = QLCDNumber(FormSystem)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.lcdNumber.setFont(font1)
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setProperty("value", 1.000000000000000)

        self.horizontalLayout.addWidget(self.lcdNumber)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FormSystem)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.progressBarCPU = QProgressBar(FormSystem)
        self.progressBarCPU.setObjectName(u"progressBarCPU")
        self.progressBarCPU.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBarCPU)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(FormSystem)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 0))
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.progressBarRAM = QProgressBar(FormSystem)
        self.progressBarRAM.setObjectName(u"progressBarRAM")
        self.progressBarRAM.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBarRAM)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(FormSystem)

        QMetaObject.connectSlotsByName(FormSystem)
    # setupUi

    def retranslateUi(self, FormSystem):
        FormSystem.setWindowTitle(QCoreApplication.translate("FormSystem", u"\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("FormSystem", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("FormSystem", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU:", None))
        self.label_3.setText(QCoreApplication.translate("FormSystem", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM:", None))
    # retranslateUi

