from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import sys
from PacketTracer import Ui_Form
class mywindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(mywindow,self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)





def main():
    app = QApplication(sys.argv)
    window = mywindow()
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()