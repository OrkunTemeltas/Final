import sys
from decimal import Decimal

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


def solve_circuit(V, Rs, Ls, Cs, t=0):
    I1 = Vd/R1d

    # calculation

    return 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('10 Gozlu RLC reis')
        self.setGeometry(50, 50, 1000, 500)
        self.UI()

        self.V = 0
        self.Rs = 0
        self.Cs = 0
        self.Ls = 0
        self.t = 0

    def UI(self):
        # window
        title = QLabel('10 Gözlü RLC', self)
        title.move(430, 10)
        title.setFont(QFont('Times', 20))

        # circuit
        self.devre = QLabel(self)
        self.devre.setPixmap(QPixmap('RLC.png'))
        self.devre.move(100, 50)

        # inputs
        self.V = QLineEdit(self)
        self.Vt = QLabel('V:', self)
        self.Vt.move(420, 312)
        self.V.move(440, 312)
        self.V.resize(40, 20)

        # Radiobutton for time seleciton
        self.timet = QLabel("Time:", self)
        self.timet.move(130, 312)
        self.timeZero = QRadioButton("t = 0", self)
        self.timeZero.move(190, 310)
        self.timeInfi = QRadioButton("t = ∞", self)
        self.timeInfi.move(270, 310)

        # component selector
        self.component = QComboBox(self)
        self.componentT = QLabel("Pick a component: ", self)
        self.componentT.move(70, 340)
        self.component.move(187, 337)

        elements = []
        for i in range(5):
            elements.append(f'L{i+1}')
            elements.append(f'C{i+1}')

            C1 = QLineEdit(self)
            C1.setObjectName(f'C{i+1}')

            C1t = QLabel(f'C{i+1}:', self)
            C1t.move(470+i*80, 280)
            C1.move(500+i*80, 280)
            C1.resize(40, 20)

            L = QLineEdit(self)
            L.setObjectName(f'L{i+1}')

            Lt = QLabel(f'L{i+1}:', self)
            Lt.move(70+i*80, 280)
            L.move(100+i*80, 280)
            L.resize(40, 20)

        for i in range(10):
            elements.append(f'R{i+1}')
            R = QLineEdit(self)
            Rt = QLabel(f'R{i+1}:', self)
            Rt.move(70+i*80, 250)
            R.move(100+i*80, 250)
            R.resize(40, 20)

        elements.sort()
        self.component.addItems(elements)

        # click button 'calculate'
        self.button = QPushButton("Calculate", self)
        self.button.move(770, 350)
        self.button.clicked.connect(self.calculate_all)

        # calulations
    def calculate_all(self):
        try:
            V = self.read_value('V')
            Rs = self.read_values('R', 10)
            Cs = self.read_values('C', 5)
            Ls = self.read_values('L', 5)
            t = 0

            solve_circuit(V, Rs, Ls, Cs, t)

        except:
            pass

    def read_values(self, prefix, count, type=QLineEdit):
        result = []
        for i in range(count):
            result.append(self.read_value(f'{prefix}{i+1}'))

        return result

    def read_value(self, name, type=QLineEdit):
        text = self.findChild(type, name).text()
        try:
            return Decimal(text)
        except:
            raise Exception(f'Error - Please provide a number for {name}.')


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())


# main
main()
