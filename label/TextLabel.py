from PyQt5 import QtWidgets, QtCore


class TextLabel(QtWidgets.QLabel):
    def __init__(self, resztaWidth, height, infPanelHeight, window):
        super().__init__(window)
        self.width = 500
        self.resztaWidth = resztaWidth
        self.height = height

        self.setGeometry(resztaWidth, infPanelHeight+27, self.width, height)
        self.setStyleSheet("background-color: #15b48c; font-size: 15px; qproperty-alignment: AlignJustify")
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
