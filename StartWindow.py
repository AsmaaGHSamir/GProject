# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(971, 540)
        Form.setMinimumSize(QtCore.QSize(971, 540))
        Form.setMaximumSize(QtCore.QSize(971, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/startpic.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 981, 561))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 90, 651, 81))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(17, 21, 255);\n"
"background-color: rgb(206, 217, 255);")
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(220, 230, 531, 31))
        self.progressBar.setStyleSheet("\n"
"QProgressBar{\n"
"    color: rgb(23, 58, 255);\n"
"border: 2px solid grey;\n"
"border-radius: 5px;\n"
"text-align: center;\n"
"color: white\n"
"}\n"
"QProgressBar::chunk{\n"
"background: rgb(23, 23, 255);\n"
"width: 2.25px;\n"
"margin: 0.5px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Starting"))
        self.label.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/startpic.PNG\"/></p></body></html>"))
        self.label_2.setText(_translate("Form", "  Network  Scanner and Sniffer V1.0"))

import start_rc
