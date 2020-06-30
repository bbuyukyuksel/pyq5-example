from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtWidgets import QCheckBox, QLabel
import sys

class Dialog(QDialog):
    onClosed = QtCore.pyqtSignal()
    def __init__(self, pos:QtCore.QPoint=QtCore.QPoint(400,400)):
        super().__init__()
        self.items = []
        self.title = 'Examples'
        self.winIcon = 'assets/icons/home.png'
        self.left = pos.x()
        self.top = pos.y()
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
    
    def closeEvent(self, e):
        self.onClosed.emit()

    def UI(self):
        mainVBoxLayout = QVBoxLayout()
        # region group
        group = QGroupBox("What is your favorite sport?")
        group.setStyleSheet('QGroupBox{font-weight:bold;color:grey;}')
        group.setFont(QtGui.QFont('Sanserif', 13))
        hBoxLayout = QHBoxLayout()
        # item 1
        self.radiobutton1 = QCheckBox("Football")
        self.radiobutton1.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobutton1.setIcon(QtGui.QIcon('assets/icons/football.png'))
        self.radiobutton1.setIconSize(QtCore.QSize(30,30))
        self.radiobutton1.toggled.connect(self.onRadioButton)
        hBoxLayout.addWidget(self.radiobutton1)
        # item 2
        self.radiobutton2 = QCheckBox("Basketball")
        self.radiobutton2.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobutton2.setIcon(QtGui.QIcon('assets/icons/basketball.png'))
        self.radiobutton2.setIconSize(QtCore.QSize(30,30))
        self.radiobutton2.toggled.connect(self.onRadioButton)
        hBoxLayout.addWidget(self.radiobutton2)
        # item 3
        self.radiobutton3 = QCheckBox("Tennis")
        self.radiobutton3.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobutton3.setIcon(QtGui.QIcon('assets/icons/tennis.png'))
        self.radiobutton3.setIconSize(QtCore.QSize(30,30))
        self.radiobutton3.toggled.connect(self.onRadioButton)
        hBoxLayout.addWidget(self.radiobutton3)
        group.setLayout(hBoxLayout)
        mainVBoxLayout.addWidget(group)
        # endregion group 
        # region label
        self.lb_select = QLabel("...")
        self.lb_select.setFont(QtGui.QFont('Sanserif', 11))
        self.lb_select.setStyleSheet('color:green;')
        mainVBoxLayout.addWidget(self.lb_select)
        # endregion
        self.setLayout(mainVBoxLayout)

    def onRadioButton(self):
        checkBox = self.sender()
        text = checkBox.text()
        if checkBox.isChecked():
            if text not in self.items:self.items.append(text)
        else:
            if text in self.items: self.items.remove(text)
        
        if len(self.items)>0:self.lb_select.setText(','.join(self.items))

if __name__ == '__main__':
    App = QApplication(sys.argv)
    myDialog = Dialog()
    sys.exit(App.exec())