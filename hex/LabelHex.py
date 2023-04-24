import PyQt5
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap, QColorConstants
from PyQt5 import QtWidgets, QtCore
import math


def createPoly(rad, centerX, centerY):
    polygon = PyQt5.QtGui.QPolygonF()

    arc = (math.pi*2)/6

    for i in range(7):
        polygon.append(QtCore.QPointF(round(centerX+rad*math.cos(arc*i)), round((centerY+rad*math.sin(arc*i)))))

    return polygon


class LabelHex(QtWidgets.QLabel):
    def __init__(self, x_size, y_size, infPanelHeight, window):
        super().__init__(window)

        self.colors = [QColorConstants.White,
                       QColorConstants.DarkGray,
                       QColorConstants.LightGray,
                       QColorConstants.DarkYellow,
                       QColorConstants.Green,
                       QColorConstants.Magenta,
                       QColorConstants.Red,
                       QColorConstants.Cyan,
                       QColorConstants.Yellow,
                       QColorConstants.DarkMagenta,
                       QColorConstants.Black,
                       QColorConstants.Blue,
                       QColorConstants.DarkRed]

        self.width = x_size * 42 + 95
        self.gameHeight = y_size*47 + 95 + (x_size*23)
        self.height = self.gameHeight

        self.x_size = x_size
        self.y_size = y_size
        self.setGeometry(0, infPanelHeight + 27, self.width, self.height)

        self.board = [[0 for _ in range(self.x_size)] for _ in range(self.y_size)]

        self.pixMap = QPixmap(self.width, self.height)
        self.qp = QPainter()

        self.drawBoard()

    def drawBoard(self):
        self.pixMap.fill(QColor(181, 201, 91))

        self.qp.begin(self.pixMap)

        for y in range(self.y_size):
            for x in range(self.x_size - 1, -1, -1):
                pen = QPen(self.getColor(x, y))
                self.qp.setPen(pen)
                self.qp.setBrush(PyQt5.QtGui.QBrush(self.getColor(x, y)))
                square = createPoly(25, x*42+70, y*47+70+(23*(self.x_size-1-x)))
                self.qp.drawPolygon(square)

        self.qp.end()
        self.setPixmap(self.pixMap)

    def getColor(self, x, y):
        return self.colors[self.board[y][x]]
