import os

from PyQt5.QtWidgets import QAction

from hex.swiat.SwiatHex import SwiatHex
from label.ButtonLabel import ButtonLabel
from label.InfLabel import *
from label.TextLabel import TextLabel
from lattice.swiat.SwiatLattice import SwiatLattice
from PyQt5 import QtCore

from organizm.organizmy.rosliny.Barszcz_Sosnowskiego import Barszcz_Sosnowskiego
from organizm.organizmy.rosliny.Guarana import Guarana
from organizm.organizmy.rosliny.Mlecz import Mlecz
from organizm.organizmy.rosliny.Trawa import Trawa
from organizm.organizmy.rosliny.Wilcze_Jagody import Wilcze_Jagody
from organizm.organizmy.zwierze.Antylopa import Antylopa
from organizm.organizmy.zwierze.CyberOwca import CyberOwca
from organizm.organizmy.zwierze.Czlowiek import Czlowiek
from organizm.organizmy.zwierze.Lis import Lis
from organizm.organizmy.zwierze.Owca import Owca
from organizm.organizmy.zwierze.Wilk import Wilk
from organizm.organizmy.zwierze.Zolw import Zolw


class SimulatorWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        lines = None
        super().__init__()

        if args[1] is True:
            filePath = os.path.dirname(__file__) + "\\save.txt"
            file = open(filePath, 'r')
            lines = file.readlines()

        self.saveAction = None
        self.exitAction = None

        if args[1] is False:
            x_size = (QtWidgets.QInputDialog.getInt(self, "Simulator", "Podaj szerokość pola:"))[0]
            y_size = (QtWidgets.QInputDialog.getInt(self, "Simulator", "Podaj wysokość pola"))[0]
        else:
            digits = lines[1].split(';')
            x_size = int(digits[0])
            y_size = int(digits[1])

        infLabelHeight = 40
        if args[0] == 2:
            labelHeight = int(y_size * 47 + 95 + (x_size * 23))
        else:
            labelHeight = int(42 * 2 + y_size * 20)
        buttonLabelHeight = 40

        textLabelWidth = 500
        if args[0] == 2:
            mainContentWidth = x_size * 42 + 95
        else:
            mainContentWidth = x_size * 20

        width = mainContentWidth + textLabelWidth
        height = labelHeight + infLabelHeight + buttonLabelHeight + 27

        self.infLabel = InfLabel(width, infLabelHeight, self)

        if args[0] == 1:
            if args[1] is True:
                self.mainLabel = SwiatLattice(x_size, y_size, infLabelHeight, self, False)
            else:
                self.mainLabel = SwiatLattice(x_size, y_size, infLabelHeight, self, True)
        else:
            if args[1] is True:
                self.mainLabel = SwiatHex(x_size, y_size, infLabelHeight, self, False)
            else:
                self.mainLabel = SwiatHex(x_size, y_size, infLabelHeight, self, True)

        self.buttonLabel = ButtonLabel(mainContentWidth, buttonLabelHeight, infLabelHeight + labelHeight + 27, self)
        self.buttonLabel.button.clicked.connect(self.onClick)

        self.textLabel = TextLabel(mainContentWidth, labelHeight + buttonLabelHeight, infLabelHeight, self)

        self.setWindowTitle("Simulator")
        self.setGeometry(0, 35, width, height)
        self.setFixedSize(width, height)

        self.createMenuBar()
        self.setFocus()

        if args[1] is True:
            self.wczytywanieGry()

    def createMenuBar(self):
        self.createActions()
        menuBar = self.menuBar()
        fileMenu = QtWidgets.QMenu("&File", self)
        editMenu = QtWidgets.QMenu("&Edit", self)
        helpMenu = QtWidgets.QMenu("&Help", self)
        menuBar.addMenu(fileMenu)

        self.saveAction = QAction("&Save", self)
        self.saveAction.triggered.connect(self.save)
        self.exitAction = QAction("&Exit", self)
        self.exitAction.triggered.connect(self.exit)

        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        menuBar.addMenu(editMenu)
        menuBar.addMenu(helpMenu)

    def save(self):
        text = ""
        if isinstance(self.mainLabel, SwiatHex):
            text += "2\n"
        else:
            text += "1\n"
        text += str(self.mainLabel.x_size) + ";" + str(self.mainLabel.y_size) + "\n"
        text += str(self.mainLabel.results) + "\n"
        for i in self.mainLabel.getOrganizmy():
            if isinstance(i, Czlowiek):
                text += (str(i.getTypeOfOrganizm()) + ";" + str(i.polozenie_x) + ";" + str(i.polozenie_y) + ";" +
                         str(int(i.alive)) + ";" + str(i.sila) + ";" + str(i.inicjatywa) + ";" + str(i.lifeTime) + ";" +
                         str(int(i.umiejetnosc)) + ";" + str(i.timeToEndUmiejetnosc) + ";"
                         + str(i.noOfToursToNextActivation) + "\n")
            else:
                text += (str(i.getTypeOfOrganizm()) + ";" + str(i.polozenie_x) + ";" + str(i.polozenie_y) + ";" +
                         str(int(i.alive)) + ";" + str(i.sila) + ";" +
                         str(i.inicjatywa) + ";" + str(i.lifeTime) + "\n")
        filePath = os.path.dirname(__file__) + "\\save.txt"
        with open(filePath, 'w') as file:
            file.write(text)

    def exit(self):
        self.close()

    def createActions(self):
        self.saveAction = QtWidgets.QAction("&Save", self)
        self.exitAction = QtWidgets.QAction("&Exit", self)

    def onClick(self):
        if self.mainLabel.czlowiek is not None:
            if self.mainLabel.czlowiek.alive is True:
                self.mainLabel.clearResults()
                self.mainLabel.results = ("<html>Podaj kierunek człowieka strzałkami" +
                                          " lub aktywuj umiejętność przyciskiem 'U'<br></html>")
                self.mainLabel.canSetKierunekCzlowieka = True
        else:
            self.mainLabel.wykonajTure()
        self.textLabel.setText(self.mainLabel.results)
        self.setFocus()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Up:
            if self.mainLabel.canSetKierunekCzlowieka is True:
                self.mainLabel.kierunekCzlowieka = 1
                self.mainLabel.canSetKierunekCzlowieka = False
                self.mainLabel.wykonajTure()
                self.textLabel.setText(self.mainLabel.results)
        elif event.key() == QtCore.Qt.Key.Key_Right:
            if self.mainLabel.canSetKierunekCzlowieka is True:
                self.mainLabel.kierunekCzlowieka = 3
                self.mainLabel.canSetKierunekCzlowieka = False
                self.mainLabel.wykonajTure()
                self.textLabel.setText(self.mainLabel.results)
        elif event.key() == QtCore.Qt.Key.Key_Down:
            if self.mainLabel.canSetKierunekCzlowieka is True:
                self.mainLabel.kierunekCzlowieka = 5
                self.mainLabel.canSetKierunekCzlowieka = False
                self.mainLabel.wykonajTure()
                self.textLabel.setText(self.mainLabel.results)
        elif event.key() == QtCore.Qt.Key.Key_Left:
            if self.mainLabel.canSetKierunekCzlowieka is True:
                self.mainLabel.kierunekCzlowieka = 7
                self.mainLabel.canSetKierunekCzlowieka = False
                self.mainLabel.wykonajTure()
                self.textLabel.setText(self.mainLabel.results)
        elif event.key() == QtCore.Qt.Key.Key_U:
            if self.mainLabel.czlowiek is not None:
                if self.mainLabel.czlowiek.umiejetnosc is True:
                    self.mainLabel.clearResults()
                    self.mainLabel.results = "<html>Umiejętność już jest aktywna<br></html>"
                    self.textLabel.setText(self.mainLabel.results)
                elif self.mainLabel.czlowiek.noOfToursToNextActivation == 0:
                    self.mainLabel.czlowiek.umiejetnosc = True
                    self.mainLabel.czlowiek.timeToEndUmiejetnosc = 5
                    self.mainLabel.czlowiek.noOfToursToNextActivation = 11
                    self.mainLabel.kierunekCzlowieka = 0
                    self.mainLabel.canSetKierunekCzlowieka = False
                    self.mainLabel.wykonajTure()
                    self.textLabel.setText(self.mainLabel.results)
                else:
                    self.mainLabel.clearResults()
                    self.mainLabel.results = ("<html>Umiejętność można będzie aktywować dopiero po " +
                                              str(self.mainLabel.czlowiek.noOfToursToNextActivation) +
                                              " turach<br></html>")
                    self.textLabel.setText(self.mainLabel.results)

    def wczytywanieGry(self):
        filePath = os.path.dirname(__file__) + "\\save.txt"
        file = open(filePath, 'r')
        lines = file.readlines()

        self.textLabel.setText(lines[2])
        for i in range(3, len(lines), 1):
            fields = lines[i].split(';')
            umiejetnosc, timeToEndUmiejetnosc, noOfToursToNextActivation = None, None, None
            typeOfOrganizm = fields[0]
            if typeOfOrganizm == "Człowiek":
                x = int(fields[1])
                y = int(fields[2])
                alive = bool(fields[3])
                sila = int(fields[4])
                inicjatywa = int(fields[5])
                lifeTime = int(fields[6])
                umiejetnosc = bool(fields[7])
                timeToEndUmiejetnosc = int(fields[8])
                noOfToursToNextActivation = int(fields[9])
            else:
                x = int(fields[1])
                y = int(fields[2])
                alive = bool(fields[3])
                sila = int(fields[4])
                inicjatywa = int(fields[5])
                lifeTime = int(fields[6])
            organizm = self.createOrganizm(typeOfOrganizm)
            self.mainLabel.board[organizm.polozenie_y][organizm.polozenie_x] = 0
            if isinstance(organizm, Czlowiek):
                organizm.umiejetnosc = umiejetnosc
                organizm.timeToEndUmiejetnosc = timeToEndUmiejetnosc
                organizm.noOfToursToNextActivation = noOfToursToNextActivation
            organizm.sila, organizm.inicjatywa = sila, inicjatywa
            organizm.polozenie_x, organizm.polozenie_y = x, y
            organizm.alive, organizm.lifeTime = alive, lifeTime

            self.mainLabel.organizmy.append(organizm)
            organizm.rysowanie()
        self.mainLabel.rysujSwiat()

    def createOrganizm(self, typ):
        if typ == "Barszcz Sosnowskiego":
            organizm = Barszcz_Sosnowskiego(self.mainLabel)
        elif typ == "Guarana":
            organizm = Guarana(self.mainLabel)
        elif typ == "Mlecz":
            organizm = Mlecz(self.mainLabel)
        elif typ == "Trawa":
            organizm = Trawa(self.mainLabel)
        elif typ == "Wilcze Jagody":
            organizm = Wilcze_Jagody(self.mainLabel)
        elif typ == "Antylopa":
            organizm = Antylopa(self.mainLabel)
        elif typ == "Człowiek":
            organizm = Czlowiek(self.mainLabel)
        elif typ == "Lis":
            organizm = Lis(self.mainLabel)
        elif typ == "Owca":
            organizm = Owca(self.mainLabel)
        elif typ == "Wilk":
            organizm = Wilk(self.mainLabel)
        elif typ == "Żółw":
            organizm = Zolw(self.mainLabel)
        elif typ == "Cyber Owca":
            organizm = CyberOwca(self.mainLabel)
        else:
            organizm = Trawa(self.mainLabel)
        return organizm
