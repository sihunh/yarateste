import sys
import ctypes
import os
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
        #line_edit = QLineEdit(self)
        
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        #hbox.addWidget(line_edit)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        btn1.clicked.connect(self.open_browser)

        self.setWindowTitle('TOOL')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def open_browser(self):
        browser()


if __name__ == '__main__':
    ctypes.windll.kernel32.SetDllDirectoryW(None)
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())