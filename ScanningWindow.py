import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import SecondWindow
import SniffingWindow
from Scanwin import Ui_Form as thirdwind

class mainApp3(QWidget, thirdwind):
    def __init__(self, parent=None):
        super(mainApp3,self).__init__(parent)
        QWidget.__init__(self)
        self.setWindowIcon(QIcon('myicon'))
        self.setupUi(self)
        self.table2.setRowCount(0)
        self.table2.setColumnWidth(0,170)
        self.exitbtnw4.clicked.connect(exit)
        self.backbtnw4.clicked.connect(self.open_selection_win)
        self.clearbtnw4.clicked.connect(self.clear)
        self.loaddata2()

    def open_selection_win(self):
       self.close()
       self.open = SecondWindow.mainApp1()
       self.open.show()

    def loaddata2(self):
        connection = sqlite3.connect("data.db")
        cur = connection.cursor()
        #cur.execute("CREATE TABLE if not exists skills (url text, ip , mac , time)")
        cur.execute("SELECT * FROM skills ")
        connection.commit()
        result = cur.fetchall()
        tablerow2 = self.table2.rowCount()
        self.ips = set()
        for row in result:
            self.table2.setRowCount(tablerow2+1)
            if str(row[1]) not in self.ips:
                self.ips.add(row[1])
                addedip = row[1]
                self.table2.setItem(tablerow2, 0, QTableWidgetItem(addedip))
                tablerow2 += 1
            else:
                continue

        connection.close()


    def open_last_win(self):
       self.close()
       self.open = SniffingWindow.mainApp2()
       self.open.show()



    def clear(self):

        self.table2.setRowCount(0)


def main():
    app = QApplication(sys.argv)
    window = mainApp3()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()