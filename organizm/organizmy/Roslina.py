import random
from abc import ABC

from organizm.Organizm import Organizm


class Roslina(Organizm, ABC):
    def akcja(self):
        # if random.randint(0, 2) != 0:
        #     return
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

        from organizm.organizmy.rosliny.Barszcz_Sosnowskiego import Barszcz_Sosnowskiego
        from organizm.organizmy.rosliny.Guarana import Guarana
        from organizm.organizmy.rosliny.Mlecz import Mlecz
        from organizm.organizmy.rosliny.Trawa import Trawa
        from organizm.organizmy.rosliny.Wilcze_Jagody import Wilcze_Jagody
        if self.getTypeOfOrganizm() == "Barszcz Sosnowskiego":
            nowy = Barszcz_Sosnowskiego(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Guarana":
            nowy = Guarana(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Mlecz":
            nowy = Mlecz(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Trawa":
            nowy = Trawa(self.swiat, to_x, to_y)
        elif self.getTypeOfOrganizm() == "Wilcze Jagody":
            nowy = Wilcze_Jagody(self.swiat, to_x, to_y)
        else:
            nowy = Trawa(self.swiat, to_x, to_y)

        self.swiat.organizmy.append(nowy)
        nowy.rysowanie()
        self.swiat.results += "Wyrosła nowa roślina " + nowy.getTypeOfOrganizm() + "<br>"
