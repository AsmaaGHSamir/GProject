# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sniffing.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1248, 676)
        Form.setStyleSheet("background-color: rgb(169, 199, 255);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(240, 60, 991, 481))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-10, 60, 241, 481))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(37, 75, 113);\n"
"color: rgb(255, 255, 255);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border-radius: 5px;")
        self.label_3.setObjectName("label_3")
        self.erasebtn = QtWidgets.QPushButton(Form)
        self.erasebtn.setGeometry(QtCore.QRect(1030, 560, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.erasebtn.setFont(font)
        self.erasebtn.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.erasebtn.setObjectName("erasebtn")
        self.savebtn = QtWidgets.QPushButton(Form)
        self.savebtn.setGeometry(QtCore.QRect(600, 560, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.savebtn.setFont(font)
        self.savebtn.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.savebtn.setObjectName("savebtn")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(0, 620, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.backbtn = QtWidgets.QPushButton(Form)
        self.backbtn.setGeometry(QtCore.QRect(830, 630, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.backbtn.setFont(font)
        self.backbtn.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.backbtn.setObjectName("backbtn")
        self.exitbtnw3 = QtWidgets.QPushButton(Form)
        self.exitbtnw3.setEnabled(True)
        self.exitbtnw3.setGeometry(QtCore.QRect(1030, 630, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.exitbtnw3.setFont(font)
        self.exitbtnw3.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.exitbtnw3.setObjectName("exitbtnw3")
        self.updatebtn = QtWidgets.QPushButton(Form)
        self.updatebtn.setGeometry(QtCore.QRect(830, 560, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.updatebtn.setFont(font)
        self.updatebtn.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.updatebtn.setObjectName("updatebtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "URL Being Visited"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "IP"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "MAC Address"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Time"))
        self.label_3.setText(_translate("Form", "     Sniffing View"))
        self.erasebtn.setText(_translate("Form", "Erase All"))
        self.savebtn.setText(_translate("Form", "Save"))
        self.label_5.setText(_translate("Form", "   By EFAA"))
        self.backbtn.setText(_translate("Form", "Back"))
        self.exitbtnw3.setText(_translate("Form", "EXIT"))
        self.updatebtn.setText(_translate("Form", "update"))

