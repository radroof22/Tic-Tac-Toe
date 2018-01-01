# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tic_tac_toe.ui'
#
# Created: Thu Jan 21 16:44:21 2016
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
import time
import random
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    turn = 0

    box1 = 0
    box2 = 0
    box3 = 0
    box4 = 0
    box5 = 0
    box6 = 0
    box7 = 0
    box8 = 0
    box9 = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		
        self.box = QtGui.QPushButton(self.centralwidget)
        self.box.setGeometry(QtCore.QRect(100, 80, 111, 101))
        self.box.setText(_fromUtf8(""))
        self.box.setObjectName(_fromUtf8("box"))
        self.box.clicked.connect(lambda: self.box1_user(self.box,self.box1))
		
        self.box_2 = QtGui.QPushButton(self.centralwidget)
        self.box_2.setGeometry(QtCore.QRect(210, 80, 111, 101))
        self.box_2.setText(_fromUtf8(""))
        self.box_2.setObjectName(_fromUtf8("box_2"))
        self.box_2.clicked.connect(lambda: self.box2_user(self.box_2,self.box2))
		
        self.box_3 = QtGui.QPushButton(self.centralwidget)
        self.box_3.setGeometry(QtCore.QRect(320, 80, 111, 101))
        self.box_3.setText(_fromUtf8(""))
        self.box_3.setObjectName(_fromUtf8("box_3"))
        self.box_3.clicked.connect(lambda: self.box3_user(self.box_3,self.box3))
		
        self.box_4 = QtGui.QPushButton(self.centralwidget)
        self.box_4.setGeometry(QtCore.QRect(100, 180, 111, 101))
        self.box_4.setText(_fromUtf8(""))
        self.box_4.setObjectName(_fromUtf8("box_4"))
        self.box_4.clicked.connect(lambda: self.box4_user(self.box_4,self.box4))
		
        self.box_5 = QtGui.QPushButton(self.centralwidget)
        self.box_5.setGeometry(QtCore.QRect(210, 180, 111, 101))
        self.box_5.setText(_fromUtf8(""))
        self.box_5.setObjectName(_fromUtf8("box_5"))
        self.box_5.clicked.connect(lambda: self.box5_user(self.box_5, self.box5))
		
        self.box_6 = QtGui.QPushButton(self.centralwidget)
        self.box_6.setGeometry(QtCore.QRect(320, 180, 111, 101))
        self.box_6.setText(_fromUtf8(""))
        self.box_6.setObjectName(_fromUtf8("box_6"))
        self.box_6.clicked.connect(lambda: self.box6_user(self.box_6, self.box6))
		
        self.box_7 = QtGui.QPushButton(self.centralwidget)
        self.box_7.setGeometry(QtCore.QRect(100, 280, 111, 101))
        self.box_7.setText(_fromUtf8(""))
        self.box_7.setObjectName(_fromUtf8("box_7"))
        self.box_7.clicked.connect(lambda: self.box7_user(self.box_7, self.box7))
		
        self.box_8 = QtGui.QPushButton(self.centralwidget)
        self.box_8.setGeometry(QtCore.QRect(210, 280, 111, 101))
        self.box_8.setText(_fromUtf8(""))
        self.box_8.setObjectName(_fromUtf8("box_8"))
        self.box_8.clicked.connect(lambda: self.box8_user(self.box_8, self.box8))
		
        self.box_9 = QtGui.QPushButton(self.centralwidget)
        self.box_9.setGeometry(QtCore.QRect(320, 280, 111, 101))
        self.box_9.setText(_fromUtf8(""))
        self.box_9.setObjectName(_fromUtf8("box_9"))
        self.box_9.clicked.connect(lambda: self.box9_user(self.box_9, self.box9))
		
        self.newGame = QtGui.QPushButton(self.centralwidget)
        self.newGame.setGeometry(QtCore.QRect(575, 220, 135, 81))
        self.newGame.setText(_fromUtf8(" New  Game "))
        self.newGame.setObjectName(_fromUtf8("box_9"))
        self.newGame.clicked.connect(lambda:self.restart())
				
        #self.playerWin = QtGui.QLabel(self.centralwidget)

		
        #s#elf.playerWin.setGeometry(QtCore.QRect(560, 50, 141, 81))
        ##elf.playerWin.setObjectName(_fromUtf8("playerWin"))
        self.compWins = QtGui.QLabel(self.centralwidget)
		
        self.compWins.setGeometry(QtCore.QRect(575, 130, 135, 81))
        self.compWins.setObjectName(_fromUtf8("compWins"))
        #self.tieGames = QtGui.QLabel(self.centralwidget)
		
        #self.tieGames.setGeometry(QtCore.QRect(560, 210, 141, 81))
        #self.tieGames.setObjectName(_fromUtf8("tieGames"))
        self.label = QtGui.QLabel(self.centralwidget)
        #self.winSign = QtGui.QLabel(self.centralwidget)
        #self.winSign.setGeometry(QtCore.QRect(560,210,141,81))
		
        self.label.setGeometry(QtCore.QRect(130, 0, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe", None))
        #self.playerWin.setText(_translate("MainWindow", "Player Wins: 0", None))
        self.compWins.setText(_translate("MainWindow", "", None))
        #self.winSign.setText(_translate("MainWindow", "", None))
        self.label.setText(_translate("MainWindow", "Tic Tac Toe", None))
        

    def box1_user(self, box, vari):
        if self.box1 == 2:
            pass
        elif self.turn == 0:
            self.box1 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()
        #self.computer_play()

    def box2_user(self, box, vari):
        if self.box2 == 2:
            pass
        elif self.turn == 0:
            self.box2 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()



    def box3_user(self, box, vari):
        if self.box3 == 2:
            pass
        elif self.turn == 0:
            self.box3 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()

		

    def box4_user(self, box, vari):
        if self.box4 == 2:
            pass
        elif self.turn == 0:
            self.box4 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()
 
		

    def box5_user(self, box, vari):
        if self.box5 == 2:
            pass
        elif self.turn == 0:
            self.box5 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()

		

    def box6_user(self, box, vari):
        if self.box6 == 2:
            pass
        elif self.turn == 0:
            self.box6 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()

		

    def box7_user(self, box, vari):
        if self.box7 == 2:
            pass
        elif self.turn == 0:
            self.box7 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()

		

    def box8_user(self, box, vari):
        if self.box8 == 2:
            pass
        elif self.turn == 0:
            self.box8 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()
		
    def box9_user(self, box, vari):
        if self.box9 == 2:
            pass
        elif self.turn == 0:
            self.box9 = 1
            box.setText("X")
            self.turn = 1
        self.checkWin()
        if self.win == None:
            self.computer_play()



    def box1_cpu(self):
        if self.turn == 1:
            self.box1 = 2
            self.box.setText("O")
            self.turn = 0
            self.checkWin()

    def box2_cpu(self):
        if self.turn == 1:
            self.box2 = 2
            self.box_2.setText("O")
            self.turn = 0
            self.checkWin()


    def box3_cpu(self):
        if self.turn == 1:
            self.box3 = 2
            self.box_3.setText("O")
            self.turn = 0
            self.checkWin()
		

    def box4_cpu(self):
        if self.turn == 1:
            self.box4 = 2
            self.box_4.setText("O")
            self.turn = 0
            self.checkWin()
		

    def box4_cpu(self):
        if self.turn == 1: 
            self.box4 = 2
            self.box_4.setText("O")
            self.turn = 0
            self.checkWin()
		

    def box5_cpu(self):
        if self.turn == 1: 
            self.box5 = 2
            self.box_5.setText("O")
            self.turn = 0
            self.checkWin()
		

    def box6_cpu(self):
        if self.turn == 1:
            self.box6 = 2
            self.box_6.setText("O")
            self.turn = 0
            self.checkWin()
		

    def box7_cpu(self):
        if self.turn == 1: 
            self.box7 = 2
            self.box_7.setText("O")
            self.turn = 0
            self.checkWin()
		

    def box8_cpu(self):
        if self.turn == 1: 
            self.box8 = 2
            self.box_8.setText("O")
            self.turn = 0
            self.checkWin()
		
    def box9_cpu(self):
        if self.turn == 1:
            self.box9 = 2
            self.box_9.setText("O")
            self.turn = 0
            self.checkWin()

    def checkWin(self):
        self.win_msg = None
        self.win = None 



        if self.box1 == self.box2 == self.box3 and self.box1 != 0:
           

            if self.box1 == 1:
                self.win = 'Player'
            elif self.box1 == 2:
                self.win = 'Computer'
				
				
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))

        elif self.box1 == self.box4 == self.box7 and self.box1 != 0:

            if self.box1 == 1:
                self.win = 'Player'
            elif self.box1 == 2:
                self.win = 'Computer'
				
            		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))

        elif self.box3 == self.box6 == self.box9 and self.box3 != 0:
            if self.box3 == 1:
                self.win = 'Player'
            elif self.box3 == 2:
                self.win = 'Computer'
           
            		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))

        elif self.box7 == self.box8 == self.box9 and self.box7 != 0:
            if self.box7 == 1:
                self.win = 'Player'
            elif self.box7 == 2:
                self.win = 'Computer'
            		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))
            
        elif self.box4 == self.box5 == self.box6 and self.box4 != 0:
            if self.box4 == 1:
                self.win = 'Player'
            elif self.box4 == 2:
                self.win = 'Computer'

            		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))
        elif self.box1 == self.box5 == self.box9 and self.box1 != 0:
		
            if self.box1 == 1:
                self.win = 'Player'
            elif self.box1 == 2:
                self.win = 'Computer'
           		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))
       
        elif self.box3 == self.box5 == self.box7 and self.box3 != 0:
            if self.box3 == 1:
                self.win = 'Player'
            elif self.box3 == 2:
                self.win = 'Computer'
           		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))
             
        elif self.box2 == self.box5 == self.box8 and self.box2 != 0:
            if self.box2 == 1:
                self.win = 'Player'
            elif self.box2 == 2:
                self.win = 'Computer'
           		
            self.win = str(self.win) + " Won Game"
            
            
            self.compWins.setText(str(self.win))
            
        elif self.box1 and self.box2 and self.box3 and self.box4 and self.box5 and self.box6 and self.box7 and self.box8 and self.box9 != 0:
            self.msg = "It's a tie!!!"
            		
            
            
            
            self.compWins.setText(str(self.msg))
		#Causes infinite loop (below)

			
    def computer_play(self):



        if self.box1 == self.box2 and self.box1 == 1 and self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()
        elif self.box1 == self.box3 and self.box1 == 1 and self.box2 == 0:
            self.box2 = 2
            self.box2_cpu()
        elif self.box2 == self.box3 and self.box3==1 and self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()

        elif self.box1 == self.box4 and self.box1==1 and self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()
        elif self.box1 == self.box7 and self.box1 == 1 and self.box4 == 0:
            self.box4 = 2
            self.box4_cpu()
        elif self.box4 == self.box7 and self.box7==1 and self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()

        elif self.box3 == self.box6 and self.box3==1 and self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()
        elif self.box3 == self.box9 and self.box3 == 1 and self.box6 == 0:
            self.box6 = 2
            self.box6_cpu()
        elif self.box6 == self.box9 and self.box9==1 and self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()

        elif self.box7 == self.box8 and self.box7==1 and self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()
        elif self.box7 == self.box9 and self.box9 ==1 and self.box8 == 0:
            self.box8 = 2
            self.box8_cpu()
        elif self.box8 == self.box9 and self.box9==1 and self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()

        elif self.box4 == self.box5 and self.box4==1 and self.box6 == 0:
            self.box6 = 2
            self.box6_cpu()
        elif self.box4 == self.box6 and self.box6 == 1 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box6 and self.box6==1 and self.box4 == 0:
            self.box4 = 2
            self.box4_cpu()

        elif self.box1 == self.box5 and self.box1==1 and self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()
        elif self.box1 == self.box9 and self.box9 == 1 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box9 and self.box9==1 and self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()

        elif self.box3 == self.box5 and self.box3==1 and self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()
        elif self.box3 == self.box7 and self.box7==1 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box7 and self.box7==1 and self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()

        elif self.box2 == self.box5 and self.box2 == 1 and self.box8 == 0:
            self.box8 = 2
            self.box8_cpu()
        elif self.box2 == self.box8 and self.box8 == 1 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box8 and self.box8 == 1 and self.box2 == 0: 
            self.box2 = 2
            self.box2_cpu()

        elif self.box1 == self.box2 and self.box1 == 2 and self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()
        elif self.box1 == self.box3 and self.box1 == 2 and self.box2 == 0:
            self.box2 = 2 
            self.box2_cpu()
        elif self.box2 == self.box3 and self.box3==2 and self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()

        elif self.box1 == self.box4 and self.box1==2 and self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()
        elif self.box1 == self.box7 and self.box1 == 2 and self.box4 == 0:
            self.box4 = 2
            self.box4_cpu()
        elif self.box4 == self.box7 and self.box4==2 and self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()

        elif self.box3 == self.box6 and self.box3==2 and self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()
        elif self.box3 == self.box9 and self.box3 == 2 and self.box6 == 0:
            self.box6 = 2
            self.box6_cpu()
        elif self.box6 == self.box9 and self.box9==2 and self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()

        elif self.box7 == self.box8 and self.box7==2 and self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()
        elif self.box7 == self.box9 and self.box9 ==2 and self.box8 == 0:
            self.box8 = 2
            self.box8_cpu()
        elif self.box8 == self.box9 and self.box9==2 and self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()

        elif self.box4 == self.box5 and self.box4==2 and self.box6 == 0:
            self.box6 = 2
            self.box6_cpu()
        elif self.box4 == self.box6 and self.box6 == 2 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box6 and self.box6==2 and self.box4 == 0:
            self.box4 = 2
            self.box4_cpu()

        elif self.box1 == self.box5 and self.box1==2 and self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()
        elif self.box1 == self.box9 and self.box9 == 2 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box9 and self.box9==2 and self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()

        elif self.box3 == self.box5 and self.box3==2 and self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()
        elif self.box3 == self.box7 and self.box7==2 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box7 and self.box7==2 and self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()

        elif self.box2 == self.box5 and self.box2 == 2 and self.box8 == 0:
            self.box8 = 2
            self.box8_cpu()
        elif self.box2 == self.box8 and self.box8 == 2 and self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()
        elif self.box5 == self.box8 and self.box5 == 2 and self.box2 == 0: 
            self.box2 = 2
            self.box2_cpu()

        elif self.box5 == 0:
            self.box5 = 2
            self.box5_cpu()

        elif self.box1 == 0:
            self.box1 = 2
            self.box1_cpu()
        elif self.box3 == 0:
            self.box3 = 2
            self.box3_cpu()
        elif self.box7 == 0:
            self.box7 = 2
            self.box7_cpu()
        elif self.box9 == 0:
            self.box9 = 2
            self.box9_cpu()

        else:
            choice = random.randint(1,9)
            if choice == 1 and self.box1 != 1 or 2:
                self.box1 = 2
                self.box1_cpu()
            elif choice == 2 and self.box2 != 1 or 2:
                self.box2 = 2
                self.box2_cpu()
            elif choice == 3 and self.box3 != 1 or 2:
                self.box3 = 2
                self.box3_cpu()
            elif choice == 2 and self.box4 != 1 or 2:
                self.box4 = 2
                self.box4_cpu()
            elif choice == 2 and self.box5 != 1 or 2:
                self.box5 = 2
                self.box5_cpu()
            elif choice == 2 and self.box6 != 1 or 2:
                self.box6 = 2
                self.box6_cpu()
            elif choice == 2 and self.box7 != 1 or 2:
                self.box7 = 2
                self.box7_cpu()
            elif choice == 2 and self.box8 != 1 or 2:
                self.box8 = 2
                self.box8_cpu()
            elif choice == 2 and self.box9 != 1 or 2:
                self.box9 = 2
                self.box9_cpu()
        self.checkWin()

    def restart(self):
        self.box1 = 0
        self.box2 = 0
        self.box3= 0
        self.box4 = 0
        self.box5 = 0
        self.box6 = 0
        self.box7 = 0
        self.box8 = 0
        self.box9 = 0
		
        self.box.setText("")
        self.box_2.setText("")
        self.box_3.setText("")
        self.box_4.setText("")
        self.box_5.setText("")
        self.box_6.setText("")
        self.box_7.setText("")
        self.box_8.setText("")
        self.box_9.setText("")
        self.compWins.setText("")


            




	

#if __name__ == "__main__":
 #   import sys
  #  app = QtGui.QApplication(sys.argv)
   # MainWindow = QtGui.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())

def main():
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

def new():
    main()
main()

