from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QButtonGroup, QHBoxLayout, QLayout
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100, 400, 100)
        self.setWindowTitle('QButtonGroup')

        self.UI()

        self.show()

    def UI(self):
        hBox = QHBoxLayout()

        self.buttonGroup = QButtonGroup(self)

        button = QPushButton('test1')
        self.buttonGroup.addButton(button,1)
        button = QPushButton('test2')
        self.buttonGroup.addButton(button,2)

        hBox.addLayout(self.buttonGroup)
        self.setLayout(hBox)
        

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())