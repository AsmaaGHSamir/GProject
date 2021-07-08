# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scanwin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(777, 480)
        Form.setMinimumSize(QtCore.QSize(404, 298))
        Form.setStyleSheet("background-color: rgb(80, 161, 241);")
        self.table2 = QtWidgets.QTableWidget(Form)
        self.table2.setGeometry(QtCore.QRect(410, 40, 261, 301))
        self.table2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        self.table2.setFont(font)
        self.table2.setStyleSheet("background-color: rgb(208, 203, 200);\n"
"background-color: rgb(211, 238, 255);\n"
"background-color: rgb(189, 216, 255);")
        self.table2.setIconSize(QtCore.QSize(10, 0))
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(1)
        self.table2.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table2.setHorizontalHeaderItem(0, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 20pt \"Rage Italic\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 251, 361))
        self.label_2.setStyleSheet("background-color: rgb(57, 114, 171);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.exitbtnw4 = QtWidgets.QPushButton(Form)
        self.exitbtnw4.setGeometry(QtCore.QRect(460, 430, 181, 31))
        self.exitbtnw4.setStyleSheet("QPushButton{\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 80, 121);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.exitbtnw4.setObjectName("exitbtnw4")
        self.backbtnw4 = QtWidgets.QPushButton(Form)
        self.backbtnw4.setGeometry(QtCore.QRect(460, 390, 181, 31))
        self.backbtnw4.setStyleSheet("QPushButton{\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 80, 121);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.backbtnw4.setObjectName("backbtnw4")
        self.clearbtnw4 = QtWidgets.QPushButton(Form)
        self.clearbtnw4.setGeometry(QtCore.QRect(460, 350, 181, 31))
        self.clearbtnw4.setStyleSheet("QPushButton{\n"
"border-radius: 3px;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 80, 121);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.clearbtnw4.setObjectName("clearbtnw4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scanning"))
        item = self.table2.verticalHeaderItem(0)
        item.setText(_translate("Form", "D0"))
        item = self.table2.verticalHeaderItem(1)
        item.setText(_translate("Form", "D1"))
        item = self.table2.verticalHeaderItem(2)
        item.setText(_translate("Form", "D2"))
        item = self.table2.verticalHeaderItem(3)
        item.setText(_translate("Form", "D3"))
        item = self.table2.verticalHeaderItem(4)
        item.setText(_translate("Form", "D4"))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Connected IPs"))
        self.label.setText(_translate("Form", "   By EFAA"))
        self.label_2.setText(_translate("Form", "     Scanning View"))
        self.exitbtnw4.setText(_translate("Form", "Exit"))
        self.backbtnw4.setText(_translate("Form", "Back"))
        self.clearbtnw4.setText(_translate("Form", "Clear"))

