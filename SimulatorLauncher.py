import os
from PyQt5 import QtWidgets

from SimulatorWindow.SimulatorWindow import SimulatorWindow
from buttons.MenuButton import *


class SimulatorLauncher(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.simulatorWindow = None
        self.setGeometry(200, 200, 500, 750)
        self.setWindowTitle("Simulator")

        sngl = MenuButton("Start new game in lattice", 100, self)
        sngl.clicked.connect(self.openLattice)

        sngh = MenuButton("Start new game in hex", 250, self)
        sngh.clicked.connect(self.openHex)

        cont = MenuButton("Continue", 400, self)
        cont.setGeometry(125, 400, 250, 100)
        cont.setEnabled(os.path.isfile(os.path.dirname(__file__) + "\\SimulatorWindow\\save.txt"))
        cont.clicked.connect(self.contin)

        ext = MenuButton("Exit", 550, self)
        ext.setGeometry(125, 550, 250, 100)
        ext.clicked.connect(self.exitFromGame)

    def openLattice(self):
        self.hide()
        self.simulatorWindow = SimulatorWindow(1, False)
        self.simulatorWindow.show()
        self.close()

    def openHex(self):
        self.hide()
        self.simulatorWindow = SimulatorWindow(2, False)
        self.simulatorWindow.show()
        self.close()

    def contin(self):
        try:
            filePath = os.path.dirname(__file__) + "\\SimulatorWindow\\save.txt"
            with open(filePath) as file:
                typ = int(file.readline())
                self.hide()
                self.simulatorWindow = SimulatorWindow(typ, True)
                self.simulatorWindow.show()
                self.close()
        except FileNotFoundError:
            print("Save file don't exist")

    def exitFromGame(self):
        self.close()
