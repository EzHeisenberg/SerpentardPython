import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QListWidget, QGridLayout, QVBoxLayout, QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car



ecole_epsi = Ecole("EPSI")

c1 = Car(50, "car n°1", ecole_epsi.nom_ecole(), "Marseille")
c2 = Car(60, "car n°2", ecole_epsi.nom_ecole(), "Marseille")
c3 = Car(25, "car n°3", ecole_epsi.nom_ecole(), "Marseille")
list_de_car = [c1, c2, c3]



class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("School Car manager")

        


    def initUI(self):
        vbox = QVBoxLayout(self)

        listWidget = QListWidget()

        listWidget.addItem("sparrow")
        listWidget.addItem("robin")
        listWidget.addItem("crow")
        listWidget.addItem("raven")
        listWidget.addItem("woodpecker")
        listWidget.addItem("hummingbird")

        listWidget.itemDoubleClicked.connect(self.onClicked)

        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QListWidget')
        self.show()

    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Window()
    #mainWin.showMaximized()
    sys.exit( app.exec_() )