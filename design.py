# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_habitWidget(object):
    def setupUi(self, habitWidget):
        if not habitWidget.objectName():
            habitWidget.setObjectName(u"habitWidget")
        habitWidget.resize(654, 344)
        self.layoutWidget = QWidget(habitWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 290, 365, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelInputHabit = QLabel(self.layoutWidget)
        self.labelInputHabit.setObjectName(u"labelInputHabit")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.labelInputHabit.setFont(font)

        self.horizontalLayout.addWidget(self.labelInputHabit)

        self.textInputHabit = QLineEdit(self.layoutWidget)
        self.textInputHabit.setObjectName(u"textInputHabit")

        self.horizontalLayout.addWidget(self.textInputHabit)

        self.addButton = QPushButton(self.layoutWidget)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.saveButton = QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.loadButton = QPushButton(self.layoutWidget)
        self.loadButton.setObjectName(u"loadButton")

        self.horizontalLayout.addWidget(self.loadButton)

        self.groupBox = QGroupBox(habitWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 631, 281))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"border: 1px solid black;")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 21, 611, 251))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(310)

        self.retranslateUi(habitWidget)

        QMetaObject.connectSlotsByName(habitWidget)
    # setupUi

    def retranslateUi(self, habitWidget):
        habitWidget.setWindowTitle(QCoreApplication.translate("habitWidget", u"Form", None))
        self.labelInputHabit.setText(QCoreApplication.translate("habitWidget", u"Habit:", None))
        self.addButton.setText(QCoreApplication.translate("habitWidget", u"Add", None))
        self.saveButton.setText(QCoreApplication.translate("habitWidget", u"Save", None))
        self.loadButton.setText(QCoreApplication.translate("habitWidget", u"Load", None))
        self.groupBox.setTitle(QCoreApplication.translate("habitWidget", u"Habits", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("habitWidget", u"Habits", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("habitWidget", u"Dates", None));
    # retranslateUi

