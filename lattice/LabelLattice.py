from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap, QColorConstants
from PyQt5 import QtWidgets


class LabelLattice(QtWidgets.QLabel):
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

        self.width = x_size * 20
        self.gameHeight = 42 * 2 + y_size * 20
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
            for x in range(self.x_size):
                pen = QPen(self.getColor(x, y))
                self.qp.setPen(pen)
                self.qp.fillRect(x*20+1, 42 + y*20 + 1, 18, 18, self.getColor(x, y))

        self.qp.end()
        self.setPixmap(self.pixMap)

    def getColor(self, x, y):
        return self.colors[self.board[y][x]]
