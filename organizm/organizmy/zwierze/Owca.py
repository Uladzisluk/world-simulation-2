from organizm.organizmy.Zwierze import Zwierze


class Owca(Zwierze):
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

    def rysowanie(self):
        self.swiat.board[self.polozenie_y][self.polozenie_x] = 2

    def getTypeOfOrganizm(self):
        return "Owca"
