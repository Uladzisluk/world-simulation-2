from organizm.organizmy.Zwierze import Zwierze


class Czlowiek(Zwierze):
    umiejetnosc = False
    timeToEndUmiejetnosc = 0
    noOfToursToNextActivation = 0

    def __init__(self, *args):
        self.sila = 5
        self.inicjatywa = 4
        self.lifeTime = 0
        self.alive = True
        self.swiat = args[0]
        self.swiat.czlowiek = self
        nowePolozenie = self.randomizePolozenie()
        self.polozenie_x, self.polozenie_y = nowePolozenie[0], nowePolozenie[1]
        self.rysowanie()

    def akcja(self):
        if self.noOfToursToNextActivation != 0:
            self.noOfToursToNextActivation = self.noOfToursToNextActivation - 1
        if self.timeToEndUmiejetnosc != 0:
            self.timeToEndUmiejetnosc = self.timeToEndUmiejetnosc - 1
        else:
            self.umiejetnosc = False

        to_x, to_y, kolizjaResult = 0, 0, 1

        if self.swiat.kierunekCzlowieka == 1:
            to_x, to_y = self.polozenie_x, self.polozenie_y - 1
        elif self.swiat.kierunekCzlowieka == 3:
            to_x, to_y = self.polozenie_x + 1, self.polozenie_y
        elif self.swiat.kierunekCzlowieka == 5:
            to_x, to_y = self.polozenie_x, self.polozenie_y + 1
        elif self.swiat.kierunekCzlowieka == 7:
            to_x, to_y = self.polozenie_x - 1, self.polozenie_y
        else:
            self.lifeTime = self.lifeTime + 1
            return
        if to_x < 0 or to_x >= self.swiat.x_size or to_y < 0 or to_y >= self.swiat.y_size:
            return

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
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 6

    def getTypeOfOrganizm(self):
        return "Człowiek"
