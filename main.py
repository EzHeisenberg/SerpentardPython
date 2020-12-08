import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Classe.Ecole import Ecole
from Classe.Promotion import Promotion
from Classe.Eleve import Eleve
from Classe.Professeur import Prof
from Classe.Car import Car

app = QApplication.instance()
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = QWidget()

# la fenêtre est rendue visible
fen.show()

# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()