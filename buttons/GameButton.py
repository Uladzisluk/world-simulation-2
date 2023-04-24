from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class GameButton(QPushButton):
    def __init__(self, widget, height):
        super().__init__(widget)
        self.setFixedSize(150, height)
        self.setText("Nowa Tura")
        self.setFont(QFont("TimesRoman", 15))
        self.setStyleSheet("background-color: #696969; foreground-color: white")