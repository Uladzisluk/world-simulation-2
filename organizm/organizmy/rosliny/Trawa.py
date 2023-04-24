import random

from organizm.organizmy.Roslina import Roslina


class Trawa(Roslina):
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

    def kolizja(self, atakujacy):
        self.swiat.toRemove.append(self)
        self.alive = False
        self.swiat.results += (atakujacy.getTypeOfOrganizm() + " zjadł " + self.getTypeOfOrganizm() + "<br>")
        return 1

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 7

    def getTypeOfOrganizm(self):
        return "Trawa"
