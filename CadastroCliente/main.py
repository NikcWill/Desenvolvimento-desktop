import sys



from tools.import show
from PySide6.QtWidgets import QApplication
from CadastroCliente.controller.cliente_dao import DataBase
from CadastroCliente.view.tela_principal import MainWindow

db = DataBase()
db.connect()
db.create_table_cliente()
db.close_connection()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()