from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import sys
from decimal import Decimal

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('10 Gozlu RLC reis')
        self.setGeometry(50,50,1000,500)
        self.UI()
        
        
    
    def UI(self):
        #window
        title = QLabel('10 Gözlü RLC',self)
        title.move(430,10)
        title.setFont(QFont('Times',20))
        
        #circuit
        self.devre = QLabel(self)
        self.devre.setPixmap(QPixmap('RLC.png'))
        self.devre.move(100,50)
        
        #inputs
        self.R1 = QLineEdit(self)
        self.R1t = QLabel('R1:',self)
        self.R1t.move(70,250)
        self.R1.move(100,250)
        self.R1.resize(40,20)
        
        self.R2 = QLineEdit(self)
        self.R2t = QLabel('R2:',self)
        self.R2t.move(150,250)
        self.R2.move(180,250)
        self.R2.resize(40,20)
        
        self.R3 = QLineEdit(self)
        self.R3t = QLabel('R3:',self)
        self.R3t.move(230,250)
        self.R3.move(260,250)
        self.R3.resize(40,20)
        
        self.R4 = QLineEdit(self)
        self.R4t = QLabel('R4:',self)
        self.R4t.move(310,250)
        self.R4.move(340,250)
        self.R4.resize(40,20)
        
        self.R5 = QLineEdit(self)
        self.R5t = QLabel('R5:',self)
        self.R5t.move(390,250)
        self.R5.move(420,250)
        self.R5.resize(40,20)
        
        self.R6 = QLineEdit(self)
        self.R6t = QLabel('R6:',self)
        self.R6t.move(470,250)
        self.R6.move(500,250)
        self.R6.resize(40,20)
        
        self.R7 = QLineEdit(self)
        self.R7t = QLabel('R7:',self)
        self.R7t.move(550,250)
        self.R7.move(580,250)
        self.R7.resize(40,20)
        
        self.R8 = QLineEdit(self)
        self.R8t = QLabel('R8:',self)
        self.R8t.move(630,250)
        self.R8.move(660,250)
        self.R8.resize(40,20)
        
        self.R9 = QLineEdit(self)
        self.R9t = QLabel('R9:',self)
        self.R9t.move(710,250)
        self.R9.move(740,250)
        self.R9.resize(40,20)
        
        self.R10 = QLineEdit(self)
        self.R10t = QLabel('R10:',self)
        self.R10t.move(790,250)
        self.R10.move(820,250)
        self.R10.resize(40,20)
        
        self.L1 = QLineEdit(self)
        self.L1t = QLabel('L1:',self)
        self.L1t.move(70,280)
        self.L1.move(100,280)
        self.L1.resize(40,20)
        
        self.L2 = QLineEdit(self)
        self.L2t = QLabel('L2:',self)
        self.L2t.move(150,280)
        self.L2.move(180,280)
        self.L2.resize(40,20)
        
        self.L3 = QLineEdit(self)
        self.L3t = QLabel('L3:',self)
        self.L3t.move(230,280)
        self.L3.move(260,280)
        self.L3.resize(40,20)
        
        self.L4 = QLineEdit(self)
        self.L4t = QLabel('L4:',self)
        self.L4t.move(310,280)
        self.L4.move(340,280)
        self.L4.resize(40,20)
        
        self.L5 = QLineEdit(self)
        self.L5t = QLabel('L5:',self)
        self.L5t.move(390,280)
        self.L5.move(420,280)
        self.L5.resize(40,20)
        
        self.C1 = QLineEdit(self)
        self.C1t = QLabel('C1:',self)
        self.C1t.move(470,280)
        self.C1.move(500,280)
        self.C1.resize(40,20)
        
        self.C2 = QLineEdit(self)
        self.C2t = QLabel('C2:',self)
        self.C2t.move(550,280)
        self.C2.move(580,280)
        self.C2.resize(40,20)
        
        self.C3 = QLineEdit(self)
        self.C3t = QLabel('C3:',self)
        self.C3t.move(630,280)
        self.C3.move(660,280)
        self.C3.resize(40,20)
        
        self.C4 = QLineEdit(self)
        self.C4t = QLabel('C4:',self)
        self.C4t.move(710,280)
        self.C4.move(740,280)
        self.C4.resize(40,20)
        
        self.C5 = QLineEdit(self)
        self.C5t = QLabel('C5:',self)
        self.C5t.move(790,280)
        self.C5.move(820,280)
        self.C5.resize(40,20)
        
        self.V = QLineEdit(self)
        self.Vt = QLabel('V:',self)
        self.Vt.move(420,312)
        self.V.move(440,312)
        self.V.resize(40,20)
        
        #Radiobutton for time seleciton
        self.timet = QLabel("Time:",self)
        self.timet.move(130,312)
        self.timeZero = QRadioButton("t = 0",self)
        self.timeZero.move(190,310)
        self.timeInfi = QRadioButton("t = ∞",self)
        self.timeInfi.move(270,310)
        
        #component selector
        self.component = QComboBox(self)
        self.componentT = QLabel("Pick a component: ",self)
        self.componentT.move(70,340)
        self.component.move(187,337)
        
        self.component.addItem('R1')
        self.component.addItem('R2')
        self.component.addItem('R3')
        self.component.addItem('R4')
        self.component.addItem('R5')
        self.component.addItem('R6')
        self.component.addItem('R7')
        self.component.addItem('R8')
        self.component.addItem('R9')
        self.component.addItem('R10')
    
        self.component.addItem('L1')
        self.component.addItem('L2')
        self.component.addItem('L3')
        self.component.addItem('L4')
        self.component.addItem('L5')
    
        self.component.addItem('C1')
        self.component.addItem('C2')
        self.component.addItem('C3')
        self.component.addItem('C4')
        self.component.addItem('C5')
        
        self.component.addItem('A1')
        self.component.addItem('A2')
        self.component.addItem('A3')
        self.component.addItem('A4')
        self.component.addItem('A5')
        self.component.addItem('A6')
        self.component.addItem('A7')
        self.component.addItem('A8')
        self.component.addItem('A9')
        self.component.addItem('A10')
        
        #click button 'calculate'
        self.button = QPushButton("Calculate",self)
        self.button.move(770,350)
        self.button.clicked.connect(self.calculate_all)
        
        #calulations
    def calculate_all(self):
        R1d = Decimal(self.R1.text())
        Vd  = Decimal(self.V.text())
        I1 = Vd/R1d
        R1output = "I1: {:.2f} VR1: {:.2f}".format(I1,Vd)
        
        
        
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec_())

# main
main()