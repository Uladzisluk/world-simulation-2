from organizm.organizmy.Roslina import Roslina
from organizm.organizmy.zwierze.Czlowiek import Czlowiek


class Wilcze_Jagody(Roslina):
    def __init__(self, *args):
        self.sila = 99
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
        self.swiat.toRemove.append(atakujacy)
        self.alive = False
        atakujacy.alive = False
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 0
        if isinstance(atakujacy, Czlowiek) is True:
            self.swiat.czlowiek = None
        self.swiat.results += (atakujacy.getTypeOfOrganizm() + " zjadł " + self.getTypeOfOrganizm() + " i zaginął<br>")
        return 0

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 10

    def getTypeOfOrganizm(self):
        return "Wilcze Jagody"
