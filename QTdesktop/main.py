import sys
from PySide6 import *
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
principal = MainWindow()
principal.show()
app.exec()