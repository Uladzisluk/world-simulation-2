import random

from organizm.organizmy.zwierze.Czlowiek import *


class Antylopa(Zwierze):

    def __init__(self, *args):
        self.sila = 4
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
        if self.swiat.isCellInGameMapAroundCoordinate(self.polozenie_x, self.polozenie_y, 2) is False:
            self.lifeTime = self.lifeTime + 1
            return

        kolizjaResult = 1
        while True:
            kierunek = random.randint(0, 7)
            match kierunek:
                case 0:
                    to_x, to_y = self.polozenie_x - 2, self.polozenie_y - 2
                case 1:
                    to_x, to_y = self.polozenie_x, self.polozenie_y - 2
                case 2:
                    to_x, to_y = self.polozenie_x + 2, self.polozenie_y - 2
                case 3:
                    to_x, to_y = self.polozenie_x + 2, self.polozenie_y
                case 4:
                    to_x, to_y = self.polozenie_x + 2, self.polozenie_y + 2
                case 5:
                    to_x, to_y = self.polozenie_x, self.polozenie_y + 2
                case 6:
                    to_x, to_y = self.polozenie_x - 2, self.polozenie_y + 2
                case 7:
                    to_x, to_y = self.polozenie_x - 2, self.polozenie_y
                case _:
                    to_x, to_y = self.polozenie_x, self.polozenie_y
            if 0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size:
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
                if random.randint(0, 1) == 0 and self.swiat.isFreeCellAroundCoordinate(to_x, to_y, 1) is True:
                    self.uciecOdWalki(organizm, to_x, to_y)
                    kolizjaResult = 2
                else:
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

    def kolizja(self, atakujacy):
        if self.getTypeOfOrganizm() == atakujacy.getTypeOfOrganizm():
            self.nowyOrganizm(atakujacy)
            return 2

        if random.randint(0, 1) == 0:
            if self.swiat.isFreeCellAroundCoordinate(self.polozenie_x, self.polozenie_y, 1):
                self.uciecOdWalki(atakujacy, self.polozenie_x, self.polozenie_y)
                return 1
        if self.czyOdbilAtak(atakujacy) is True:
            self.swiat.toRemove.append(atakujacy)
            atakujacy.alive = False
            self.swiat.results += ("W walce pomiędzy " + self.getTypeOfOrganizm() + " a " +
                                   atakujacy.getTypeOfOrganizm() + " zwyciężył " + self.getTypeOfOrganizm() + "<br>")
            return 0
        else:
            self.swiat.toRemove.append(self)
            self.alive = False
            self.swiat.results += ("W walce pomiędzy " + self.getTypeOfOrganizm() + " a " +
                                   atakujacy.getTypeOfOrganizm() +
                                   " zwyciężył " + atakujacy.getTypeOfOrganizm() + "<br>")
            return 1

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 5

    def getTypeOfOrganizm(self):
        return "Antylopa"

    def uciecOdWalki(self, atakujacy, x, y):
        self.swiat.results += (self.getTypeOfOrganizm() + " uciekła przed walką z " +
                               atakujacy.getTypeOfOrganizm() + " na sąsiednie pole<br>")
        while True:
            kierunek = random.randint(0, 7)
            match kierunek:
                case 0:
                    to_x, to_y = x - 1, y - 1
                case 1:
                    to_x, to_y = x, y - 1
                case 2:
                    to_x, to_y = x + 1, y - 1
                case 3:
                    to_x, to_y = x + 1, y
                case 4:
                    to_x, to_y = x + 1, y + 1
                case 5:
                    to_x, to_y = x, y + 1
                case 6:
                    to_x, to_y = x - 1, y + 1
                case 7:
                    to_x, to_y = x - 1, y
                case _:
                    to_x, to_y = x, y
            if (0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size and
                    self.swiat.board[to_y][to_x] == 0):
                break
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 0
        self.polozenie_x = to_x
        self.polozenie_y = to_y
        self.rysowanie()
