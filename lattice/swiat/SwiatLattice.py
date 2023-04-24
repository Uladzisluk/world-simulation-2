from PyQt5.QtGui import QMouseEvent
from PyQt5 import QtWidgets

from lattice.LabelLattice import LabelLattice
from organizm.organizmy.rosliny.Barszcz_Sosnowskiego import Barszcz_Sosnowskiego
from organizm.organizmy.rosliny.Guarana import Guarana
from organizm.organizmy.rosliny.Mlecz import Mlecz
from organizm.organizmy.rosliny.Trawa import Trawa
from organizm.organizmy.rosliny.Wilcze_Jagody import Wilcze_Jagody
from organizm.organizmy.zwierze.Antylopa import Antylopa
from organizm.organizmy.zwierze.CyberOwca import CyberOwca
from organizm.organizmy.zwierze.Czlowiek import Czlowiek
from organizm.organizmy.zwierze.Lis import Lis
from organizm.organizmy.zwierze.Owca import Owca
from organizm.organizmy.zwierze.Wilk import Wilk
from organizm.organizmy.zwierze.Zolw import Zolw


class SwiatLattice(LabelLattice):
    def __init__(self, x_size, y_size, infPanelHeight, window, newGame):
        super().__init__(x_size, y_size, infPanelHeight, window)

        self.window = window
        self.organizmy = []
        self.toRemove = []
        self.results = ""
        self.czlowiek = None
        self.kierunekCzlowieka = 0
        self.canSetKierunekCzlowieka = False

        if newGame is True:
            self.generowanieSwiata()
        self.rysujSwiat()

    def wykonajTure(self):
        self.results = "<html>"
        self.sortOrganizmy()
        numberOfOrganizms = len(self.organizmy)
        for i in range(numberOfOrganizms):
            current = self.organizmy[i]
            if current.alive is True:
                current.akcja()
        for i in self.toRemove:
            self.organizmy.remove(i)
        self.toRemove.clear()
        self.results += "</html>"
        self.rysujSwiat()

    def rysujSwiat(self):
        self.drawBoard()

    def getOrganizmy(self):
        return self.organizmy

    def getAllZwierzetaAroundCoordinate(self, x, y):
        organizms = []
        if 0 <= y-1 < self.y_size and 0 <= x-1 < self.x_size and 0 < self.board[y - 1][x - 1] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x - 1, y - 1))
        if 0 <= y-1 < self.y_size and 0 <= x < self.x_size and 0 < self.board[y - 1][x] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x, y - 1))
        if 0 <= y-1 < self.y_size and 0 <= x+1 < self.x_size and 0 < self.board[y - 1][x + 1] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x + 1, y - 1))
        if 0 <= y < self.y_size and 0 <= x+1 < self.x_size and 0 < self.board[y][x + 1] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x + 1, y))
        if 0 <= y+1 < self.y_size and 0 <= x+1 < self.x_size and 0 < self.board[y + 1][x + 1] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x + 1, y + 1))
        if 0 <= y+1 < self.y_size and 0 <= x < self.x_size and 0 < self.board[y + 1][x] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x, y + 1))
        if 0 <= y+1 < self.y_size and 0 <= x-1 < self.x_size and 0 < self.board[y + 1][x - 1] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x - 1, y + 1))
        if 0 <= y < self.y_size and 0 <= x-1 < self.x_size and 0 < self.board[y][x - 1] < 7:
            organizms.append(self.whatOrganizmOnCoordinate(x - 1, y))
        return organizms

    def whatOrganizmOnCoordinate(self, x, y):
        for i in self.organizmy:
            if i.polozenie_x == x and i.polozenie_y == y and i.alive is True:
                return i
        return None

    def sortOrganizmy(self):
        for i in range(len(self.organizmy)):
            x = self.organizmy[i]
            j = i
            while j > 0 and (x.inicjatywa > self.organizmy[j - 1].inicjatywa or (
                    x.inicjatywa == self.organizmy[j - 1].inicjatywa and x.lifeTime >= self.organizmy[j - 1].lifeTime)):
                self.organizmy[j] = self.organizmy[j - 1]
                j = j - 1
            self.organizmy[j] = x

    def isFreeCell(self):
        for i in self.board:
            for j in i:
                if j == 0:
                    return True
        return False

    def isFreeCellAroundCoordinate(self, x, y, distance):
        if (0 <= x - distance < self.x_size and 0 <= y - distance < self.y_size and
                self.board[y - distance][x - distance] == 0):
            return True
        elif 0 <= x < self.x_size and 0 <= y - distance < self.y_size and self.board[y - distance][x] == 0:
            return True
        elif (0 <= x + distance < self.x_size and 0 <= y - distance < self.y_size and
              self.board[y - distance][x + distance] == 0):
            return True
        elif 0 <= x + distance < self.x_size and 0 <= y < self.y_size and self.board[y][x + distance] == 0:
            return True
        elif (0 <= x + distance < self.x_size and 0 <= y + distance < self.y_size and
              self.board[y + distance][x + distance] == 0):
            return True
        elif 0 <= x < self.x_size and 0 <= y + distance < self.y_size and self.board[y + distance][x] == 0:
            return True
        elif (0 <= x - distance < self.x_size and 0 <= y + distance < self.y_size and
              self.board[y + distance][x - distance] == 0):
            return True
        elif 0 <= x - distance < self.x_size and 0 <= y < self.y_size and self.board[y][x - distance] == 0:
            return True
        else:
            return False

    def isCellInGameMapAroundCoordinate(self, x, y, distance):
        if 0 <= x - distance < self.x_size and 0 <= y - distance < self.y_size:
            return True
        elif 0 <= x < self.x_size and 0 <= y - distance < self.y_size:
            return True
        elif 0 <= x + distance < self.x_size and 0 <= y - distance < self.y_size:
            return True
        elif 0 <= x + distance < self.x_size and 0 <= y < self.y_size:
            return True
        elif 0 <= x + distance < self.x_size and 0 <= y + distance < self.y_size:
            return True
        elif 0 <= x < self.x_size and 0 <= y + distance < self.y_size:
            return True
        elif 0 <= x - distance < self.x_size and 0 <= y + distance < self.y_size:
            return True
        elif 0 <= x - distance < self.x_size and 0 <= y < self.y_size:
            return True
        else:
            return False

    def clearResults(self):
        self.results = ""

    def generowanieSwiata(self):
        if self.isFreeCell():
            self.organizmy.append(Czlowiek(self))
        if self.isFreeCell():
            self.organizmy.append(Owca(self))
        if self.isFreeCell():
            self.organizmy.append(Wilk(self))
        if self.isFreeCell():
            self.organizmy.append(Zolw(self))
        if self.isFreeCell():
            self.organizmy.append(Trawa(self))
        if self.isFreeCell():
            self.organizmy.append(Wilk(self))
        if self.isFreeCell():
            self.organizmy.append(Trawa(self))

    def mousePressEvent(self, event: QMouseEvent):
        x = int(event.x() / 20)
        y = int((event.y() - 42) / 20)

        if 0 <= x < self.x_size and 0 <= y < self.y_size and self.board[y][x] == 0:
            organizm = None
            org = (QtWidgets.QInputDialog.getInt(self, "Simulator", "Podaj organizm:\n" +
                                                 "1.Antylopa   2.Lis\n3.Owca  4.Wilk   5.Żółw\n" +
                                                 "6.Barszcz Sosnowskiego\n7.Guarana   8.Mlecz\n" +
                                                 "9.Trawa   10.Wilcze Jagody\n11.Cyber Owca"))[0]
            match org:
                case 1:
                    organizm = Antylopa(self, x, y)
                case 2:
                    organizm = Lis(self, x, y)
                case 3:
                    organizm = Owca(self, x, y)
                case 4:
                    organizm = Wilk(self, x, y)
                case 5:
                    organizm = Zolw(self, x, y)
                case 6:
                    organizm = Barszcz_Sosnowskiego(self, x, y)
                case 7:
                    organizm = Guarana(self, x, y)
                case 8:
                    organizm = Mlecz(self, x, y)
                case 9:
                    organizm = Trawa(self, x, y)
                case 10:
                    organizm = Wilcze_Jagody(self, x, y)
                case 11:
                    organizm = CyberOwca(self, x, y)
                case _:
                    pass

            if organizm is not None:
                self.organizmy.append(organizm)
            self.rysujSwiat()
            self.clearResults()
            if organizm is not None:
                self.results += ("<html>Został utworzony " + organizm.getTypeOfOrganizm() +
                                 " na {" + str(x) + "," + str(y) + "}<br></html>")
            self.window.textLabel.setText(self.results)

    def isBarszczInGame(self):
        for i in self.organizmy:
            if i.getTypeOfOrganizm() == "Barszcz Sosnowskiego":
                return True
        return False
