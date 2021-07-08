from PyQt5.QtWidgets import *
import sys
import SniffingWindow
import ScanningWindow
from second_win import Ui_select_operation

class mainApp1(QFrame, Ui_select_operation):
    def __init__(self, parent=None):
        super(mainApp1, self).__init__(parent)
        QFrame.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Network Scanner and Sniffer V1.0")
        self.setToolTip('The main program')
        self.scanbtn.clicked.connect(self.open_scanning_win)
        self.scanbtn.setToolTip('Start Scanning')
        self.sniffbtn.clicked.connect(self.open_sniffing_win)
        self.sniffbtn.setToolTip('Start Sniffing')
        self.exitbtnw2.setToolTip('Click To Exit')
        self.exitbtnw2.clicked.connect(exit)

    def open_scanning_win(self):
        self.close()
        self.open = ScanningWindow.mainApp3()
        self.open.show()


    def open_sniffing_win(self):
        self.close()
        self.open = SniffingWindow.mainApp2()
        self.open.show()


def main():
    app = QApplication(sys.argv)
    window = mainApp1()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
