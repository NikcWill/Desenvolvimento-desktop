import sys

from Tools.scripts.dutree import show
from PySide6.QtWidgets import QApplication
from Desenvolvimento_desktop.Desenvolvimento_desktop.CadastroCliente.controller.cliente_dao import DataBase
from Desenvolvimento_desktop.Desenvolvimento_desktop.CadastroCliente.view.tela_principal import MainWindow

db = DataBase()
db.connect()
db.create_table_cliente()
db.close_connection()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()