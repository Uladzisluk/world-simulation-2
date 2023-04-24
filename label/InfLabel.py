import PyQt5.QtCore
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import *


class InfLabel(QtWidgets.QLabel):
    def __init__(self, width, height, window):
        super().__init__(window)
        self.width = width
        self.setText("Uladzislau Lukashevich, nr. 191608")
        self.setFont(QtGui.QFont("Arial", int(height / 2)))
        self.setStyleSheet("background-color: #b5c95b")
        self.setGeometry(0, 27, width, height)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
