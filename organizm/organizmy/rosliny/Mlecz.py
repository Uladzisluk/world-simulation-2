import random

from organizm.organizmy.Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, *args):
        self.sila = 0
        self.inicjatywa = 0
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
        for i in range(3):
            if random.randint(0, 2) != 0:
                return
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
                if (0 <= to_x < self.swiat.x_size and 0 <= to_y < self.swiat.y_size and
                        self.swiat.board[to_y][to_x] == 0):
                    break

            nowy = Mlecz(self.swiat, to_x, to_y)

            self.swiat.organizmy.append(nowy)
            nowy.rysowanie()
            self.swiat.results += "Wyrosła nowa roślina " + nowy.getTypeOfOrganizm() + "<br>"

    def kolizja(self, atakujacy):
        self.swiat.toRemove.append(self)
        self.alive = False
        self.swiat.results += (atakujacy.getTypeOfOrganizm() + " zjadł " +
                               self.getTypeOfOrganizm() + "<br>")
        return 1

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 8

    def getTypeOfOrganizm(self):
        return "Mlecz"
