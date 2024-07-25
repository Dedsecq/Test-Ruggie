from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel

from final_win import *


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.connects()  # Встановлює зв'язки між елементами
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle('Test Ruffice')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lbl1 = QLabel(txt_name)
        self.lbl2 = QLabel(txt_age)
        self.lbl3 = QLabel(txt_test1)
        self.lbl4 = QLabel(txt_test2)
        self.lbl5 = QLabel(txt_test3)
        self.lbl6 = QLabel('hh:mm:ss')

        self.btn1 = QPushButton(txt_starttest1)
        self.btn2 = QPushButton(txt_starttest2)
        self.btn3 = QPushButton(txt_starttest3)
        self.btn4 = QPushButton(txt_sendresults)

        self.le1 = QLineEdit()
        self.le2 = QLineEdit()
        self.le3 = QLineEdit()
        self.le4 = QLineEdit()
        self.le5 = QLineEdit()

        self.v1 = QVBoxLayout()
        self.v2 = QVBoxLayout()
        self.hline = QHBoxLayout()

        self.v1.addWidget(self.lbl1, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.le1, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.lbl2, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.le2, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.lbl3, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.btn1, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.le3, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.lbl4, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.btn2, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.lbl5, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.btn3, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.le4, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.le5, alignment=Qt.AlignLeft)
        self.v1.addWidget(self.btn4, alignment=Qt.AlignCenter)

        self.v2.addWidget(self.lbl6, alignment=Qt.AlignLeft)

        self.hline.addLayout(self.v1)
        self.hline.addLayout(self.v2)
        self.setLayout(self.hline)


    def next_click(self):
        self.hide()
        self.fw = FinaltWin()
    
    def connects(self):
        self.btn4.clicked.connect(self.next_click)
