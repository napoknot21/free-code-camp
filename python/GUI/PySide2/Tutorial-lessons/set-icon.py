from PySide2.QtWidgets import QApplication, QWidget
import sys
from PySide2.QtGui import QIcon

class SetIcon (QWidget) :

    #Constructor function
    def __init__ (self) :
        super().__init__()
        self.loadProperties()
        


    def loadProperties (self):
        self.setWindowTitle("My application")
        self.setGeometry(300, 300, 500, 400)


    def setIcon (self) :
        appIcon = QIcon("userphoto.jpeg")
        self.setWindowIcon(appIcon)



myApp = QApplication(sys.argv)
W = SetIcon()
W.show()

myApp.exec_()
sys.exit(0)