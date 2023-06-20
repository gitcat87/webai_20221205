 ## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton
from ex02 import macro
import pyautogui

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.button = QPushButton("매크로시작")
        self.button.clicked.connect(macro)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        pyautogui.click(x=464, y=422, duration=2)
        pyautogui.move(0, 150)


    def initUI(self):
        self.setWindowTitle('매크로프로그램')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())