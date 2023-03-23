import sys
import requests
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #configurar janela
        self.setWindowTitle('Consulta endereço')
        self.setGeometry(100, 100, 500, 250)

        #Label de inserção  de cep
        self.lbl_cep = QLabel('Insira o cep', self)

        #Text box do cep
        self.txt_cep = QLineEdit(self)

        #Botão de consulta
        self.btn_consulta = QPushButton('Consultar', self)

        #Botão de Limpar
        self.btn_limpar = QPushButton('Limpar consulta', self)

        #Label de endereço

        self.lbl_logradoura = QLabel('', self)
        self.lbl_bairro = QLabel('', self)
        self.lbl_municipio = QLabel('', self)
        self.lbl_uf = QLabel('', self)

        #Configuração

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.layout.addWidget(self.lbl_cep, 0, 0)
        self.layout.addWidget(self.txt_cep, 0, 1)
        self.layout.addWidget(self.btn_consulta, 0, 2)
        self.layout.addWidget(self.btn_limpar, 0, 3)
        self.layout.addWidget(self.lbl_logradoura, 1, 0)
        self.layout.addWidget(self.lbl_bairro, 2, 0)
        self.layout.addWidget(self.lbl_municipio, 3, 0)
        self.layout.addWidget(self.lbl_uf, 4, 0)

        #Ações do botão

        self.btn_consulta.clicked.connect(self.consultar_cep)
        self.btn_limpar.clicked.connect(self.limpar_conteudo)
    def consultar_cep(self):
        cep = self.txt_cep.text()
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            endereco = response.json()
            self.lbl_logradoura.setText(f"Rua {endereco['logradouro']}")
            self.lbl_bairro.setText(f"Bairro {endereco['bairro']}")
            self.lbl_municipio.setText(f"Municipio {endereco['localidade']}")
            self.lbl_uf.setText(f"Estado{endereco['uf']}")
        else:
            msg = QMessageBox()
            msg.setInformativeText('Cep invalido ou não encontrado')
            msg.exec()

    def limpar_conteudo(self):
        self.lbl_logradoura.setText('')
        self.lbl_bairro.setText('')
        self.lbl_municipio.setText('')
        self.lbl_uf.setText('')
        self.txt_cep.setText('')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
