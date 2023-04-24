import math
import random

from organizm.organizmy.Zwierze import Zwierze


class CyberOwca(Zwierze):
    def __init__(self, *args):
        self.sila = 11
        self.inicjatywa = 4
        self.lifeTime = 0
        self.alive = True
        self.swiat = args[0]
        if len(args) == 1:
            nowePolozenie = self.randomizePolozenie()
            self.polozenie_x, self.polozenie_y = nowePolozenie[0], nowePolozenie[1]
        else:
            self.polozenie_x, self.polozenie_y = args[1], args[2]
        self.rysowanie()

    def akcja(self):
        to_x, to_y, kolizjaResult = 0, 0, 1
        if self.swiat.isBarszczInGame() is True:
            nearestBarszcz = self.getNearestBarszcz()

            if nearestBarszcz.polozenie_x > self.polozenie_x and nearestBarszcz.polozenie_y < self.polozenie_y:
                to_x, to_y = self.polozenie_x+1, self.polozenie_y-1
            elif nearestBarszcz.polozenie_x > self.polozenie_x and nearestBarszcz.polozenie_y > self.polozenie_y:
                to_x, to_y = self.polozenie_x + 1, self.polozenie_y + 1
            elif nearestBarszcz.polozenie_x < self.polozenie_x and nearestBarszcz.polozenie_y > self.polozenie_y:
                to_x, to_y = self.polozenie_x - 1, self.polozenie_y + 1
            elif nearestBarszcz.polozenie_x < self.polozenie_x and nearestBarszcz.polozenie_y < self.polozenie_y:
                to_x, to_y = self.polozenie_x - 1, self.polozenie_y - 1
            elif nearestBarszcz.polozenie_x == self.polozenie_x and nearestBarszcz.polozenie_y < self.polozenie_y:
                to_x, to_y = self.polozenie_x, self.polozenie_y - 1
            elif nearestBarszcz.polozenie_x == self.polozenie_x and nearestBarszcz.polozenie_y > self.polozenie_y:
                to_x, to_y = self.polozenie_x, self.polozenie_y + 1
            elif nearestBarszcz.polozenie_x > self.polozenie_x and nearestBarszcz.polozenie_y == self.polozenie_y:
                to_x, to_y = self.polozenie_x + 1, self.polozenie_y
            elif nearestBarszcz.polozenie_x < self.polozenie_x and nearestBarszcz.polozenie_y == self.polozenie_y:
                to_x, to_y = self.polozenie_x - 1, self.polozenie_y

        else:
            kierunek, to_x, to_y, kolizjaResult = 0, 0, 0, 1

            while True:
                kierunek = random.randint(0, 7)
                match kierunek:
                    case 0:
                        to_x, to_y = self.polozenie_x - 1, self.polozenie_y - 1
                    case 1:
                        to_x, to_y = self.polozenie_x, self.polozenie_y - 1
                    case 2:
                        to_x, to_y = self.polozenie_x + 1, self.polozenie_y - 1
                    case 3:
                        to_x, to_y = self.polozenie_x + 1, self.polozenie_y
                    case 4:
                        to_x, to_y = self.polozenie_x + 1, self.polozenie_y + 1
                    case 5:
                        to_x, to_y = self.polozenie_x, self.polozenie_y + 1
                    case 6:
                        to_x, to_y = self.polozenie_x - 1, self.polozenie_y + 1
                    case 7:
                        to_x, to_y = self.polozenie_x - 1, self.polozenie_y
                    case _:
                        to_x, to_y = self.polozenie_x, self.polozenie_y
                if 0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size:
                    break

        if self.swiat.board[to_y][to_x] != 0:
            from organizm.organizmy.zwierze.Czlowiek import Czlowiek
            organizm = self.swiat.whatOrganizmOnCoordinate(to_x, to_y)
            if isinstance(organizm, Czlowiek):
                if organizm.umiejetnosc is True:
                    self.swiat.board[self.polozenie_y][self.polozenie_x] = 0
                    nowePolozenie = self.przesunNaSasiedniePoleOd(to_x, to_y)
                    to_x, to_y = nowePolozenie[0], nowePolozenie[1]
                    self.swiat.results += (self.getTypeOfOrganizm() + " został przestraszony przez " +
                                           organizm.getTypeOfOrganizm() +
                                           " i przemieścił się na sąsiednie pole<br>")

        if self.swiat.board[to_y][to_x] != 0:
            organizm = self.swiat.whatOrganizmOnCoordinate(to_x, to_y)
            if organizm is not None and organizm.alive is True:
                kolizjaResult = organizm.kolizja(self)
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 0

        if kolizjaResult == 0:
            return
        elif kolizjaResult == 1:
            self.polozenie_x = to_x
            self.polozenie_y = to_y
            self.lifeTime = self.lifeTime + 1
        elif kolizjaResult == 2:
            self.lifeTime = self.lifeTime + 1
        self.rysowanie()

    def getNearestBarszcz(self):
        nearestBarsz = None
        smallestDistance = None
        for i in self.swiat.organizmy:
            if i.getTypeOfOrganizm() == "Barszcz Sosnowskiego":
                x = int(abs(self.polozenie_x - i.polozenie_x))
                y = int(abs(self.polozenie_y - i.polozenie_y))
                distance = math.sqrt(x**2 + y**2)
                if smallestDistance is None or smallestDistance >= distance:
                    smallestDistance = distance
                    nearestBarsz = i
        return nearestBarsz

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 12

    def getTypeOfOrganizm(self):
        return "Cyber Owca"
