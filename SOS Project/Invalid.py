import sys
from PyQt4 import QtGui, QtCore

class Invalid(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)

        self.b1 = QtGui.QPushButton('flash splash')
        self.b1.clicked.connect(self.flashSplash)

        layout.addWidget(self.b1)

    def flashSplash(self):
        # Be sure to keep a reference to the SplashScreen
        # otherwise it'll be garbage collected
        # That's why there is 'self.' in front of the name
        self.splash = QtGui.QSplashScreen(QtGui.QPixmap('Invalidmove.png'))

        # SplashScreen will be in the center of the screen by default.
        # You can move it to a certain place if you want.
        # self.splash.move(10,10)

        self.splash.show()

        # Close the SplashScreen after 2 secs (2000 ms)
        QtCore.QTimer.singleShot(1500, self.splash.close)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Dialog()
    main.show()

    sys.exit(app.exec_())