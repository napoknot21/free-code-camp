from PySide2.QtWidgets import QApplication, QWidget
import time
import sys


class Window (QWidget) :

    def __init__ (self) :
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(300, 300, 300, 300)
        #self.setMinimumHeight(100)
        #self.setMinimumWidth(250)
        #self.setMaximumHeight(200)
        #self.setMaximumWidth(800)


myApp = QApplication(sys.argv)
W = Window()
W.show()

time.sleep(5)
W.resize(600, 400)


myApp.exec_()
sys.exit(0)