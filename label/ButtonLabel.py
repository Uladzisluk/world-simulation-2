from PyQt5 import QtWidgets

from buttons.GameButton import GameButton


class ButtonLabel(QtWidgets.QLabel):
    def __init__(self, width, height, resztaHeight, window):
        super().__init__(window)
        self.button = GameButton(self, height)
        self.setGeometry(0, resztaHeight, width, height)
        self.setStyleSheet("background-color: #15b48c")
