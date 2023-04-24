import random
from abc import ABC

from organizm.Organizm import Organizm


class Zwierze(Organizm, ABC):
    def akcja(self):
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

    def kolizja(self, atakujacy):
        if self.getTypeOfOrganizm() == atakujacy.getTypeOfOrganizm():
            self.nowyOrganizm(atakujacy)
            return 2
        if self.czyOdbilAtak(atakujacy):
            self.swiat.toRemove.append(atakujacy)
            atakujacy.alive = False
            from organizm.organizmy.zwierze.Czlowiek import Czlowiek
            if isinstance(atakujacy, Czlowiek):
                self.swiat.czlowiek = None
            self.swiat.results += ("W walce pomiędzy " + self.getTypeOfOrganizm() + " a " +
                                   atakujacy.getTypeOfOrganizm() + " zwyciężył " + self.getTypeOfOrganizm() + "<br>")
            return 0
        else:
            self.swiat.toRemove.append(self)
            self.alive = False
            from organizm.organizmy.zwierze.Czlowiek import Czlowiek
            if isinstance(self, Czlowiek):
                self.swiat.czlowiek = None
            self.swiat.results += ("W walce pomiędzy " + self.getTypeOfOrganizm() + " a " +
                                   atakujacy.getTypeOfOrganizm() + " zwyciężył " +
                                   atakujacy.getTypeOfOrganizm() + "<br>")
            return 1

    def nowyOrganizm(self, atakujacy):
        if self.swiat.isFreeCellAroundCoordinate(self.polozenie_x, self.polozenie_y, 1) is False:
            return
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
            if 0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size and self.swiat.board[to_y][to_x] == 0:
                break

        from organizm.organizmy.zwierze.Antylopa import Antylopa
        from organizm.organizmy.zwierze.Lis import Lis
        from organizm.organizmy.zwierze.Owca import Owca
        from organizm.organizmy.zwierze.Wilk import Wilk
        from organizm.organizmy.zwierze.Zolw import Zolw
        if self.getTypeOfOrganizm() == "Antylopa":
            nowy = Antylopa(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Lis":
            nowy = Lis(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Owca":
            nowy = Owca(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Wilk":
            nowy = Wilk(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Żółw":
            nowy = Zolw(self.swiat, to_x, to_y)
        else:
            nowy = Owca(self.swiat, to_x, to_y)

        self.swiat.organizmy.append(nowy)
        nowy.rysowanie()
        self.swiat.results += str("Po spotkaniu " + self.getTypeOfOrganizm() + " z " + atakujacy.getTypeOfOrganizm() +
                                  " został stworzony nowy organizm<br>")

    def przesunNaSasiedniePoleOd(self, x, y):
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
            if 0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size:
                break
        polozenie = [to_x, to_y]
        return polozenie
