# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_win.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_select_operation(object):
    def setupUi(self, select_operation):
        select_operation.setObjectName("select_operation")
        select_operation.resize(700, 548)
        select_operation.setMinimumSize(QtCore.QSize(456, 374))
        select_operation.setMaximumSize(QtCore.QSize(700, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/wifi-insight-wifi-analyzer_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        select_operation.setWindowIcon(icon)
        select_operation.setWindowOpacity(1.0)
        select_operation.setStyleSheet("background-color: rgb(72, 145, 218);")
        select_operation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        select_operation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_5 = QtWidgets.QLabel(select_operation)
        self.label_5.setGeometry(QtCore.QRect(0, 500, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(select_operation)
        self.label_3.setGeometry(QtCore.QRect(100, 20, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Rage Italic")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(37, 75, 113);\n"
"font: 75 20pt \"Rage Italic\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(select_operation)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 281, 331))
        self.label_4.setObjectName("label_4")
        self.exitbtnw2 = QtWidgets.QPushButton(select_operation)
        self.exitbtnw2.setGeometry(QtCore.QRect(474, 480, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.exitbtnw2.setFont(font)
        self.exitbtnw2.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.exitbtnw2.setObjectName("exitbtnw2")
        self.groupBox_3 = QtWidgets.QGroupBox(select_operation)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 150, 231, 91))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.scanbtn = QtWidgets.QPushButton(self.groupBox_3)
        self.scanbtn.setGeometry(QtCore.QRect(40, 20, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.scanbtn.setFont(font)
        self.scanbtn.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"     box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
" box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);\n"
"color:rgd(145, 121, 0);\n"
"}")
        self.scanbtn.setObjectName("scanbtn")
        self.groupBox_4 = QtWidgets.QGroupBox(select_operation)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 250, 231, 91))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.sniffbtn = QtWidgets.QPushButton(self.groupBox_4)
        self.sniffbtn.setGeometry(QtCore.QRect(40, 20, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.sniffbtn.setFont(font)
        self.sniffbtn.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(22, 45, 68);\n"
"}\n"
"QPushButton::hover{\n"
"\n"
"color:rgd(145, 121, 0)\n"
"}")
        self.sniffbtn.setObjectName("sniffbtn")
        self.textEdit = QtWidgets.QTextEdit(select_operation)
        self.textEdit.setGeometry(QtCore.QRect(440, 110, 211, 31))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(select_operation)
        QtCore.QMetaObject.connectSlotsByName(select_operation)

    def retranslateUi(self, select_operation):
        _translate = QtCore.QCoreApplication.translate
        select_operation.setWindowTitle(_translate("select_operation", "select_operation"))
        self.label_5.setText(_translate("select_operation", "   By EFAA"))
        self.label_3.setText(_translate("select_operation", "   Network Scanner and Sniffer V1.0"))
        self.label_4.setText(_translate("select_operation", "<html><head/><body><p><img src=\":/newPrefix/wifi-insight-wifi-analyzer_icon.png\"/></p></body></html>"))
        self.exitbtnw2.setText(_translate("select_operation", "Exit"))
        self.scanbtn.setText(_translate("select_operation", "Start Scanning"))
        self.sniffbtn.setText(_translate("select_operation", "Start Sniffing"))
        self.textEdit.setHtml(_translate("select_operation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#ffffff;\">Choose to Scan or to Sniff</span></p></body></html>"))

import second_win_rc
