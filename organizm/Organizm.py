import random
from abc import ABC, abstractmethod


class Organizm(ABC):
    sila = 0
    inicjatywa = 0
    lifeTime = 0
    alive = False
    polozenie_x = 0
    polozenie_y = 0
    swiat = None

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, atakujacy):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

    @abstractmethod
    def getTypeOfOrganizm(self):
        pass

    def czyOdbilAtak(self, atakujacy):
        if self.sila > atakujacy.sila:
            return True
        else:
            return False

    def randomizePolozenie(self):
        nowePolozenie = []
        while True:
            nowePolozenie.clear()
            nowePolozenie.append(random.randint(0, self.swiat.x_size-1))
            nowePolozenie.append(random.randint(0, self.swiat.y_size-1))
            if self.swiat.board[nowePolozenie[1]][nowePolozenie[0]] == 0:
                break
        return nowePolozenie
