import interface
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.resize(800, 600)

    interface = interface.Interface()
    price = interface.getCurrentPrice("MSFT")

    label = QLabel("Price: " + str(price))
    

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()
