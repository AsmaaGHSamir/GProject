import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import sys
import SecondWindow
from StartWindow import Ui_Form
limit_time = 100
from maincode import maincode
x = threading.Thread(target = maincode)
x.start()
class EX(QThread) :
    countchange = pyqtSignal(int)

    def run(self) :
        count = 0
        while count < limit_time:
            count += 1
            time.sleep(0.6)
            self.countchange.emit(count)


class mainApp(QMainWindow, Ui_Form):
    def __init__(self, parent=None):

        super(mainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.setMaximumWidth(1800)
        self.onstart()
        self.handel_ui()


    def onstart(self):
        self.calc = EX()
        self.calc.countchange.connect(self.countchangedprogress)
        self.calc.start()

    def countchangedprogress(self, val):
        self.progressBar.setValue(val)
        if val == 100:
            time.sleep(1)
            self.closecurrentapp_opennewapp()

    def closecurrentapp_opennewapp(self):
        self.close()
        self.open = SecondWindow.mainApp1()
        self.open.show()


    def handel_ui(self):
        self.setFixedSize(973, 548)

        self.setWindowTitle('Network Scanner And Sniffer V1.0')
        self.setWindowIcon(QIcon('startpic.png'))

def main():
    app = QApplication(sys.argv)
    window = mainApp()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
