from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel
from PyQt6 import uic
from PyQt6.QtCore import *
import sys



class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("toe.ui", self)

        self.setWindowTitle("Tic Tac Toe")

        self.x_turn = True;
        self.x_first = True;

        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")

        self.label = self.findChild(QLabel, "label")

        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)


        self.show()

    def clicker(self, b):
        if(self.x_turn == True):
            b.setText("X")
            b.setEnabled(False)
            self.x_turn = False
            if(self.checkWin() == True):
                self.label.setText("X WINS")
                self.gameOver()
            elif(self.boardFull()):
                self.label.setText("TIED GAME")
            else:
                self.label.setText("O'S TURN")
        else:
            b.setText("O")
            b.setEnabled(False)
            self.x_turn = True
            if (self.checkWin()):
                self.label.setText("O WINS")
                self.gameOver()
            elif(self.boardFull()):
                self.label.setText("TIED GAME")
            else:
                self.label.setText("X'S TURN")



    def reset(self):
        button_list = [self.button1, self.button2, self.button3, self.button4, self.button5,
                       self.button6, self.button7, self.button8, self.button9]

        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            b.setStyleSheet("color: light gray;")
        if(self.x_first == True):
            self.x_first = False
            self.x_turn = False
        else:
            self.x_first = True
            self.x_turn = True

        if(self.x_turn == True):
            self.label.setText("X'S GOES FIRST")
        else:
            self.label.setText("O'S GOES FIRST")


    def gameOver(self):
        button_list = [self.button1, self.button2, self.button3, self.button4, self.button5,
                       self.button6, self.button7, self.button8, self.button9]

        for b in button_list:
            b.setEnabled(False)

    def checkWin(self):
        return self.checkvertical() or self.checkhorizontal() or self.checkacross()

    def checkvertical(self):
        if(self.button1.text() == self.button2.text() == self.button3.text()!= ""):
            self.colorGreen(self.button1, self.button2, self.button3)
            return True

        elif (self.button4.text() == self.button5.text() == self.button6.text() != ""):
            self.colorGreen(self.button4, self.button5, self.button6)
            return True

        elif(self.button7.text() == self.button8.text() == self.button9.text()!= ""):
            self.colorGreen(self.button7, self.button8, self.button9)
            return True

        return False

    def checkhorizontal(self):

        if (self.button1.text() == self.button4.text() == self.button7.text() != ""):
            self.colorGreen(self.button1, self.button4, self.button7)
            return True

        elif (self.button2.text() == self.button5.text() == self.button8.text() != ""):
            self.colorGreen(self.button2, self.button5, self.button8)
            return True

        elif (self.button3.text() == self.button6.text() == self.button9.text() != ""):
            self.colorGreen(self.button3, self.button6, self.button9)
            return True

        return False

    def checkacross(self):
        if (self.button1.text() == self.button5.text() == self.button9.text() != ""):
            self.colorGreen(self.button1, self.button5, self.button9)
            return True

        elif (self.button7.text() == self.button5.text() == self.button3.text() != ""):
            self.colorGreen(self.button7, self.button5, self.button3)
            return True
        return False

    def boardFull(self):
        button_list = [self.button1, self.button2, self.button3, self.button4, self.button5,
                       self.button6, self.button7, self.button8, self.button9]
        for b in button_list:
            if(b.isEnabled()== True):
                return False;
        return True;

    def colorGreen(self, b1, b2, b3):
        b1.setStyleSheet("color : green;")
        b2.setStyleSheet("color : green;")
        b3.setStyleSheet("color : green;")


app = QApplication([])
UIWindow = UI()

app.exec()
