from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ClickableQLabel(QLabel): #inherits from the QLabel in pyqt
 
    def __init__(self, parent):
        QLabel.__init__(self, parent)
 
    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('clicked()')) #making the label emit a signal since it doesn't by default