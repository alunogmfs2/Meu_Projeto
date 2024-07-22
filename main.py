from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMdiArea, QPushButton, QMdiSubWindow, QTextEdit
from PyQt5 import uic, QtWidgets, QtCore, QtGui
import sys

# Constantes
WIDTH = 800
HEIGHT = 600

X = 600
Y = 300


# Funcoes
def abrir(janela, janela2):
    janela2.show()
    janela.close()


class BemVindo(QMainWindow):
    def __init__(self):
        super(BemVindo, self).__init__()
        
        self.setGeometry(X, Y, WIDTH, HEIGHT)
        self.setWindowTitle("Programmers Interface")

        self.setupUi()

        self.show()
    
    def setupUi(self):
        self.Saudacao = QLabel(self)
        self.Saudacao.setGeometry(QtCore.QRect(80, 70, 621, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Saudacao.setFont(font)
        self.Saudacao.setTextFormat(QtCore.Qt.AutoText) # type: ignore
        self.Saudacao.setAlignment(QtCore.Qt.AlignCenter) # type: ignore
        self.Saudacao.setText("Seja Bem Vindo ao Programmers Interface")

        self.Comecar = QtWidgets.QPushButton(self)
        self.Comecar.setGeometry(QtCore.QRect(300, 340, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Comecar.setFont(font)
        self.Comecar.setText("Comecar")

        self.Comecar.clicked.connect(lambda: abrir(self, modos))


class Modos(QMainWindow):
    def __init__(self):
        super(Modos, self).__init__()

        self.setGeometry(X, Y, WIDTH, HEIGHT)
        self.setWindowTitle("Modos")
        
        self.label = QLabel(self)
        self.label.setText("Esta é a segunda subjanela.")
        self.label.move(100, 100)


# Initialize the App
app = QApplication(sys.argv)
bemVindo = BemVindo()
modos = Modos()
app.exec_()
