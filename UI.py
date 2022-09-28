import sys
from browser import *
from portscan import *
from out_bound_frq import *
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit)



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('browser open', self)
        btn2 = QPushButton('port scan', self)
        #line_edit = QLineEdit(self)
        btn3 = QPushButton('out bound list', self)
        
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        #hbox.addWidget(line_edit)
        hbox.addWidget(btn3)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        btn1.clicked.connect(self.open_browser)
        btn2.clicked.connect(self.port_scan)
        btn2.clicked.connect(self.out_bound)

        self.setWindowTitle('TOOL')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def open_browser(self):
        browser()

    def port_scan(self):
        self.resize(200, 250)
    
    def out_bound(self):
        self.resize(200, 250)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())