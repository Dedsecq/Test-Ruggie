from second_win import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MainWin(QWidget):
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
        self.lbl1 = QLabel(txt_hello)
        self.lbl2 = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)

        self.line = QVBoxLayout()
        self.line.addWidget(self.lbl1, alignment=Qt.AlignCenter)
        self.line.addWidget(self.lbl2, alignment=Qt.AlignCenter)
        self.line.addWidget(self.btn, alignment=Qt.AlignCenter)

        self.setLayout(self.line)

    def next_click(self):
        self.hide()
        self.sw = TestWin()

    def connects(self):
        self.btn.clicked.connect(self.next_click)


app = QApplication([])
mw = MainWin()
app.exec_()
