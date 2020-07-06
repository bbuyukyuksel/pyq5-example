from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QButtonGroup, QHBoxLayout, QLayout, QSizeGrip, QVBoxLayout

from PyQt5 import QtCore

import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100, 400, 100)
        self.setWindowTitle('QButtonGroup')
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.UI()

        self.show()

    def UI(self):
        vBox = QVBoxLayout()

        sizegrip = QSizeGrip(self)
        vBox.addWidget(sizegrip)

        self.setLayout(vBox)

        
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())