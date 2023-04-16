import sys

from PySide6.QtWidgets import QApplication
from BlocoDeNotas.controller.nota_dao import DataBase
from BlocoDeNotas.view.tela_principal import MainWindow

db = DataBase()
db.connect()
db.criar_tabela_notas()
db.close_connection()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
