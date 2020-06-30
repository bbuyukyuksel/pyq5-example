from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtWidgets import QCheckBox, QLabel, QPushButton
import sys

import window_checkbox
import window_radiobutton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.items = []
        self.title = 'Radio Button'
        self.winIcon = 'assets/icons/home.png'
        self.left = 400
        self.top = 400
        self.width = 300
        self.height = 100
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.winIcon))        
        # Init UI
        self.UI()
        self.show()

    def UI(self):
        mainVBoxLayout = QVBoxLayout()
        # region group
        group = QGroupBox("Examples")
        group.setStyleSheet('QGroupBox{font-weight:bold;color:grey;}')
        group.setFont(QtGui.QFont('Sanserif', 13))
        hBoxLayout = QHBoxLayout()
        # item 1
        self.button1 = QPushButton("Radio Box")
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.onClickedButton)
        hBoxLayout.addWidget(self.button1)
        # item 2
        self.button2 = QPushButton("Check Box")
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.onClickedButton)
        hBoxLayout.addWidget(self.button2)

        group.setLayout(hBoxLayout)
        mainVBoxLayout.addWidget(group)
        # endregion group 
        # region label
        self.lb_select = QLabel("...")
        self.lb_select.setFont(QtGui.QFont('Sanserif', 11))
        self.lb_select.setStyleSheet('color:green;')
        mainVBoxLayout.addWidget(self.lb_select)
        # endregion

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        mainWidget.setLayout(mainVBoxLayout)

    def onClickedButton(self):
        button = self.sender()
        if button is self.button1:
            '''
            ## Paralel Çalışmak için.
            self.d = window_checkbox.Dialog()
            self.d.show()
            '''
            win = window_radiobutton.Dialog(self.pos())
        elif button.objectName() == 'button2':
            win = window_checkbox.Dialog(self.pos())
        
        win.onClosed.connect(self.onWindowClosed)
        self.hide()
        win.exec()
        self.lb_select.setText(win.lb_select.text())

    @QtCore.pyqtSlot()
    def onWindowClosed(self):
        self.show()
if __name__ == '__main__':
    App = QApplication(sys.argv)
    myDialog = Window()
    sys.exit(App.exec())