from organizm.organizmy.Roslina import Roslina
from organizm.organizmy.zwierze.Czlowiek import Czlowiek


class Barszcz_Sosnowskiego(Roslina):
    def __init__(self, *args):
        self.sila = 10
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
        self.zabicWszystkichZwierzatWokol()

    def kolizja(self, atakujacy):
        if atakujacy.getTypeOfOrganizm() == "Cyber Owca":
            self.swiat.toRemove.append(self)
            self.alive = False
            self.swiat.results += (atakujacy.getTypeOfOrganizm() + " zjadł " + self.getTypeOfOrganizm() + "<br>")
            return 1
        else:
            self.swiat.toRemove.append(self)
            self.swiat.toRemove.append(atakujacy)
            self.alive = False
            atakujacy.alive = False
            if isinstance(atakujacy, Czlowiek):
                self.swiat.results += (atakujacy.getTypeOfOrganizm() + " zjadł " +
                                       self.getTypeOfOrganizm() + " i zaginął<br>")
            return 0

    def getTypeOfOrganizm(self):
        return "Barszcz Sosnowskiego"

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 11

    def zabicWszystkichZwierzatWokol(self):
        zabic = self.swiat.getAllZwierzetaAroundCoordinate(self.polozenie_x, self.polozenie_y)
        for i in zabic:
            if i.getTypeOfOrganizm() == "Cyber Owca":
                continue
            self.swiat.toRemove.append(i)
            i.alive = False
            if isinstance(i, Czlowiek):
                self.swiat.czlowiek = None
            self.swiat.board[i.polozenie_y][i.polozenie_x] = 0
            self.swiat.results += (self.getTypeOfOrganizm() + " zabił blisko stojącego " +
                                   i.getTypeOfOrganizm() + "<br>")
