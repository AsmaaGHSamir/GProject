import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
import sys
import xlsxwriter as xw
import SecondWindow
from sniffing import Ui_Form as secform

class mainApp2(QWidget, secform):
    def __init__(self, parent=None):
        super(mainApp2, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("SNIFFING")
        self.setWindowIcon(QIcon('myicon'))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0,300)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,200)
        self.tableWidget.setRowCount(0)
        self.loaddata()
        self.updatebtn.clicked.connect(self.update)
        self.exitbtnw3.clicked.connect(exit)
        self.erasebtn.clicked.connect(self.erase)
        self.savebtn.clicked.connect(self.exportToExcel)
        self.backbtn.clicked.connect(self.open_scanning_win)


    def loaddata(self):
        connection = sqlite3.connect("data.db")
        cur = connection.cursor()
        cur.execute("SELECT * FROM skills")
        connection.commit()
        result = cur.fetchall()
        tablerow = self.tableWidget.rowCount()

        for row in result:
            self.tableWidget.setRowCount(tablerow + 1)
            self.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            tablerow += 1
        connection.close()


    def exportToExcel(self):
        self.wb = xw.Workbook('analysis.xlsx')
        self.sheet = self.wb.add_worksheet('analysis')
        connection = sqlite3.connect("data.db")
        connection.commit()
        cur = connection.cursor()
        cur.execute("SELECT * FROM skills")
        result = cur.fetchall()
        i = 0
        for l,ip,mac,time in result:
            self.sheet.write(i, 0, l)
            self.sheet.write(i, 1, ip)
            self.sheet.write(i, 2, mac)
            self.sheet.write(i, 3, time)
            i += 1
        self.wb.close()
        connection.close()

    def update(self):
        self.tableWidget.setRowCount(0)
        self.loaddata()

    def deletdata(self):
        connection = sqlite3.connect("data.db")
        cur = connection.cursor()
        cur.execute('DELETE FROM skills')
        connection.commit()

    def erase(self):
        self.deletdata()
        self.tableWidget.setRowCount(0)

    def open_scanning_win(self):
        self.close()
        self.open = SecondWindow.mainApp1()
        self.open.show()

def main2():
    app = QApplication(sys.argv)
    window = mainApp2()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main2()
