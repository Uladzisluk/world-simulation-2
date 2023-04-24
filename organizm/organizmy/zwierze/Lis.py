import random

from organizm.organizmy.Zwierze import Zwierze
from organizm.organizmy.zwierze.Czlowiek import Czlowiek


class Lis(Zwierze):
    def __init__(self, *args):
        self.sila = 3
        self.inicjatywa = 7
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
        if self.isFreeCellAroundCoordinateForLis() is False:
            self.lifeTime = self.lifeTime + 1
            return
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
            if 0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size and (
                    self.swiat.board[to_y][to_x] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(to_x, to_y).sila < self.sila):
                break

        if self.swiat.board[to_y][to_x] != 0:
            organizm = self.swiat.whatOrganizmOnCoordinate(to_x, to_y)
            if isinstance(organizm, Czlowiek):
                if organizm.umiejetnosc is True:
                    self.swiat.board[self.polozenie_y][self.polozenie_x] = 0
                    nowePolozenie = self.przesunNaSasiedniePoleOd(to_x, to_y)
                    to_x, to_y = nowePolozenie[0], nowePolozenie[1]
                    self.swiat.results += (self.getTypeOfOrganizm() + " został przestraszony przez " +
                                           organizm.getTypeOfOrganizm() + " i przemieścił się na sąsiednie pole<br>")

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

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 3

    def getTypeOfOrganizm(self):
        return "Lis"

    def isFreeCellAroundCoordinateForLis(self):
        if 0 <= self.polozenie_x - 1 < self.swiat.x_size and 0 <= self.polozenie_y - 1 < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y - 1][self.polozenie_x - 1] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x - 1, self.polozenie_y - 1).sila < self.sila):
                return True
        if 0 <= self.polozenie_x < self.swiat.x_size and 0 <= self.polozenie_y - 1 < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y - 1][self.polozenie_x] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x, self.polozenie_y - 1).sila < self.sila):
                return True
        if 0 <= self.polozenie_x + 1 < self.swiat.x_size and 0 <= self.polozenie_y - 1 < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y - 1][self.polozenie_x + 1] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x + 1, self.polozenie_y - 1).sila < self.sila):
                return True
        if 0 <= self.polozenie_x + 1 < self.swiat.x_size and 0 <= self.polozenie_y < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y][self.polozenie_x + 1] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x + 1, self.polozenie_y).sila < self.sila):
                return True
        if 0 <= self.polozenie_x + 1 < self.swiat.x_size and 0 <= self.polozenie_y + 1 < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y + 1][self.polozenie_x + 1] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x + 1, self.polozenie_y + 1).sila < self.sila):
                return True
        if 0 <= self.polozenie_x < self.swiat.x_size and 0 <= self.polozenie_y + 1 < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y + 1][self.polozenie_x] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x, self.polozenie_y + 1).sila < self.sila):
                return True
        if 0 <= self.polozenie_x - 1 < self.swiat.x_size and 0 <= self.polozenie_y + 1 < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y + 1][self.polozenie_x - 1] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x - 1, self.polozenie_y + 1).sila < self.sila):
                return True
        if 0 <= self.polozenie_x - 1 < self.swiat.x_size and 0 <= self.polozenie_y < self.swiat.y_size:
            if (self.swiat.board[self.polozenie_y][self.polozenie_x - 1] == 0 or
                    self.swiat.whatOrganizmOnCoordinate(
                        self.polozenie_x - 1, self.polozenie_y).sila < self.sila):
                return True
        return False
