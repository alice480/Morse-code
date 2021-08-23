import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('morse _code.ui', self)
        self.stroka = ''
        self.morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
            'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
            'x': '-..-', 'y': '-.--', 'z': '--..'}
        self.pushButton.clicked.connect(self.print_code)
        self.pushButton_2.clicked.connect(self.print_code)
        self.pushButton_3.clicked.connect(self.print_code)
        self.pushButton_4.clicked.connect(self.print_code)
        self.pushButton_5.clicked.connect(self.print_code)
        self.pushButton_6.clicked.connect(self.print_code)
        self.pushButton_7.clicked.connect(self.print_code)
        self.pushButton_8.clicked.connect(self.print_code)
        self.pushButton_9.clicked.connect(self.print_code)
        self.pushButton_10.clicked.connect(self.print_code)
        self.pushButton_11.clicked.connect(self.print_code)
        self.pushButton_12.clicked.connect(self.print_code)
        self.pushButton_13.clicked.connect(self.print_code)
        self.pushButton_14.clicked.connect(self.print_code)
        self.pushButton_15.clicked.connect(self.print_code)
        self.pushButton_16.clicked.connect(self.print_code)
        self.pushButton_17.clicked.connect(self.print_code)
        self.pushButton_18.clicked.connect(self.print_code)
        self.pushButton_19.clicked.connect(self.print_code)
        self.pushButton_20.clicked.connect(self.print_code)
        self.pushButton_21.clicked.connect(self.print_code)
        self.pushButton_22.clicked.connect(self.print_code)
        self.pushButton_23.clicked.connect(self.print_code)
        self.pushButton_24.clicked.connect(self.print_code)
        self.pushButton_25.clicked.connect(self.print_code)
        self.pushButton_26.clicked.connect(self.print_code)

    def print_code(self):
        self.stroka += self.morse[self.sender().text()]
        self.lineEdit.setText(self.stroka)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Азбука Морзе 2")
    sys.exit(app.exec())