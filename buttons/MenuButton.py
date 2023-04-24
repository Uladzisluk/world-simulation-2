import PyQt5.QtGui
from PyQt5.QtWidgets import QPushButton


class MenuButton(QPushButton):
    def __init__(self, string, y, window):
        super().__init__(window)
        self.setText(string)
        self.setFont(PyQt5.QtGui.QFont("TimesRoman", 15))
        self.setGeometry(50, y, 400, 100)
