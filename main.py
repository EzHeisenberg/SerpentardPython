import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

fen1 = QWidget()
fen1.setWindowTitle("Manager SchoolCar 2000")
fen1.resize(800,500)
fen1.show()


app.exec_()