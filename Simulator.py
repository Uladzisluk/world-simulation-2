import sys
from SimulatorLauncher import SimulatorLauncher
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
launcher = SimulatorLauncher()
launcher.show()
sys.exit(app.exec_())
