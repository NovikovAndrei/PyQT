# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newNote_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FormNewNote(object):
    def setupUi(self, FormNewNote):
        if not FormNewNote.objectName():
            FormNewNote.setObjectName(u"FormNewNote")
        FormNewNote.resize(823, 545)
        self.verticalLayout = QVBoxLayout(FormNewNote)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayoutHeader = QHBoxLayout()
        self.horizontalLayoutHeader.setObjectName(u"horizontalLayoutHeader")
        self.labelHeader = QLabel(FormNewNote)
        self.labelHeader.setObjectName(u"labelHeader")

        self.horizontalLayoutHeader.addWidget(self.labelHeader)

        self.lineEditHeader = QLineEdit(FormNewNote)
        self.lineEditHeader.setObjectName(u"lineEditHeader")

        self.horizontalLayoutHeader.addWidget(self.lineEditHeader)


        self.verticalLayout.addLayout(self.horizontalLayoutHeader)

        self.horizontalLayoutStatusDeadline = QHBoxLayout()
        self.horizontalLayoutStatusDeadline.setObjectName(u"horizontalLayoutStatusDeadline")
        self.horizontalLayoutDeadline = QHBoxLayout()
        self.horizontalLayoutDeadline.setObjectName(u"horizontalLayoutDeadline")
        self.labelDeadline = QLabel(FormNewNote)
        self.labelDeadline.setObjectName(u"labelDeadline")

        self.horizontalLayoutDeadline.addWidget(self.labelDeadline)

        self.dateTimeEditDeadline = QDateTimeEdit(FormNewNote)
        self.dateTimeEditDeadline.setObjectName(u"dateTimeEditDeadline")
        self.dateTimeEditDeadline.setMaximumDate(QDate(9999, 12, 30))
        self.dateTimeEditDeadline.setCalendarPopup(True)

        self.horizontalLayoutDeadline.addWidget(self.dateTimeEditDeadline)


        self.horizontalLayoutStatusDeadline.addLayout(self.horizontalLayoutDeadline)

        self.groupBoxStatus = QGroupBox(FormNewNote)
        self.groupBoxStatus.setObjectName(u"groupBoxStatus")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxStatus)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButtonDone = QRadioButton(self.groupBoxStatus)
        self.radioButtonDone.setObjectName(u"radioButtonDone")

        self.horizontalLayout_4.addWidget(self.radioButtonDone)

        self.radioButtonNotDone = QRadioButton(self.groupBoxStatus)
        self.radioButtonNotDone.setObjectName(u"radioButtonNotDone")
        self.radioButtonNotDone.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButtonNotDone)


        self.horizontalLayoutStatusDeadline.addWidget(self.groupBoxStatus)


        self.verticalLayout.addLayout(self.horizontalLayoutStatusDeadline)

        self.plainTextEditNote = QPlainTextEdit(FormNewNote)
        self.plainTextEditNote.setObjectName(u"plainTextEditNote")

        self.verticalLayout.addWidget(self.plainTextEditNote)

        self.horizontalLayoutSaveCancel = QHBoxLayout()
        self.horizontalLayoutSaveCancel.setObjectName(u"horizontalLayoutSaveCancel")
        self.pushButtonSave = QPushButton(FormNewNote)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayoutSaveCancel.addWidget(self.pushButtonSave)

        self.pushButtonExit = QPushButton(FormNewNote)
        self.pushButtonExit.setObjectName(u"pushButtonExit")

        self.horizontalLayoutSaveCancel.addWidget(self.pushButtonExit)


        self.verticalLayout.addLayout(self.horizontalLayoutSaveCancel)


        self.retranslateUi(FormNewNote)

        QMetaObject.connectSlotsByName(FormNewNote)
    # setupUi

    def retranslateUi(self, FormNewNote):
        FormNewNote.setWindowTitle(QCoreApplication.translate("FormNewNote", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.labelHeader.setText(QCoreApplication.translate("FormNewNote", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a:", None))
        self.labelDeadline.setText(QCoreApplication.translate("FormNewNote", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.groupBoxStatus.setTitle(QCoreApplication.translate("FormNewNote", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.radioButtonDone.setText(QCoreApplication.translate("FormNewNote", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.radioButtonNotDone.setText(QCoreApplication.translate("FormNewNote", u"\u041d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.pushButtonSave.setText(QCoreApplication.translate("FormNewNote", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButtonExit.setText(QCoreApplication.translate("FormNewNote", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

