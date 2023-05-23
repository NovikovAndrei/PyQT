# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notes_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_FormMenuNotes(object):
    def setupUi(self, FormMenuNotes):
        if not FormMenuNotes.objectName():
            FormMenuNotes.setObjectName(u"FormMenuNotes")
        FormMenuNotes.resize(1018, 740)
        self.verticalLayout = QVBoxLayout(FormMenuNotes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelNotes = QLabel(FormMenuNotes)
        self.labelNotes.setObjectName(u"labelNotes")
        font = QFont()
        font.setPointSize(40)
        self.labelNotes.setFont(font)

        self.verticalLayout.addWidget(self.labelNotes)

        self.treeWidgetNotes = QTreeWidget(FormMenuNotes)
        font1 = QFont()
        font1.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(4, font1);
        __qtreewidgetitem.setFont(3, font1);
        __qtreewidgetitem.setFont(2, font1);
        __qtreewidgetitem.setFont(1, font1);
        __qtreewidgetitem.setFont(0, font1);
        self.treeWidgetNotes.setHeaderItem(__qtreewidgetitem)
        self.treeWidgetNotes.setObjectName(u"treeWidgetNotes")
        font2 = QFont()
        font2.setPointSize(11)
        self.treeWidgetNotes.setFont(font2)

        self.verticalLayout.addWidget(self.treeWidgetNotes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonNewNote = QPushButton(FormMenuNotes)
        self.pushButtonNewNote.setObjectName(u"pushButtonNewNote")

        self.horizontalLayout.addWidget(self.pushButtonNewNote)

        self.pushButtonDeleteNote = QPushButton(FormMenuNotes)
        self.pushButtonDeleteNote.setObjectName(u"pushButtonDeleteNote")

        self.horizontalLayout.addWidget(self.pushButtonDeleteNote)

        self.pushButtonOpenNote = QPushButton(FormMenuNotes)
        self.pushButtonOpenNote.setObjectName(u"pushButtonOpenNote")

        self.horizontalLayout.addWidget(self.pushButtonOpenNote)

        self.pushButtonEditNote = QPushButton(FormMenuNotes)
        self.pushButtonEditNote.setObjectName(u"pushButtonEditNote")

        self.horizontalLayout.addWidget(self.pushButtonEditNote)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(FormMenuNotes)

        QMetaObject.connectSlotsByName(FormMenuNotes)
    # setupUi

    def retranslateUi(self, FormMenuNotes):
        FormMenuNotes.setWindowTitle(QCoreApplication.translate("FormMenuNotes", u"\u041c\u043e\u0438 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.labelNotes.setText(QCoreApplication.translate("FormMenuNotes", u"\u041c\u043e\u0438 \u0417\u0430\u043c\u0435\u0442\u043a\u0438:", None))
        ___qtreewidgetitem = self.treeWidgetNotes.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("FormMenuNotes", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("FormMenuNotes", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("FormMenuNotes", u"\u0421\u0440\u043e\u043a \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("FormMenuNotes", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("FormMenuNotes", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None));
        self.pushButtonNewNote.setText(QCoreApplication.translate("FormMenuNotes", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.pushButtonDeleteNote.setText(QCoreApplication.translate("FormMenuNotes", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.pushButtonOpenNote.setText(QCoreApplication.translate("FormMenuNotes", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.pushButtonEditNote.setText(QCoreApplication.translate("FormMenuNotes", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
    # retranslateUi

