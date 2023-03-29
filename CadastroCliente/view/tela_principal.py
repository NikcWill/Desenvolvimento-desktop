import requests
import json
from PySide6.QtWidgets import (QMainWindow, QBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QMessageBox,
                               QSizePolicy, QVBoxLayout)

from CadastroCliente.model.cliente import Cliente
from CadastroCliente.controller.cliente_dao import  DataBase

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 300)

        self.setWindowTitle('Cadastro de cliente')

        self.lbl_sexo = QLabel()
        self.lbl_cpf = QLabel()
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask('000.000.000-00')
        self.lbl_nome = QLabel()
        self.txt_nome = QLineEdit()
        self.lbl_telefone_fixo = QLabel()
        self.txt_telefone_fixo = QLineEdit()
        self.txt_telefone_fixo.setInputMask('(00)0000-0000')
        self.lbl_telefone_celular = QLabel()
        self.txt_telefone_celular = QLineEdit()
        self.txt_telefone_celular.setInputMask('(00)00000-0000')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['não imformado', 'Masculino', 'Feminino'])
        self.lbl_cep = QLabel()
        self.txt_cep = QLineEdit()
        self.lbl_logradouro = QLabel()
        self.txt_logradouro = QLineEdit()
        self.lbl_numero = QLabel()
        self.txt_numero = QLineEdit()
        self.lbl_bairro = QLabel()
        self.txt_bairro = QLineEdit()
        self.lbl_municipio = QLabel()
        self.txt_municipio = QLineEdit()
        self.lbl_complemento = QLabel()
        self.txt_complemento = QLineEdit()
        self.lbl_estado = QLabel()
        self.txt_estado = QLineEdit()
        self.btn_salvar = QPushButton('Salvar')
        self.btn_limpar = QPushButton('Limpar')
        self.btn_remover = QPushButton('Remover')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_cpf)
        layout.addWidget(self.txt_cpf)
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.txt_nome)
        layout.addWidget(self.lbl_telefone_fixo)
        layout.addWidget(self.txt_telefone_fixo)
        layout.addWidget(self.lbl_telefone_celular)
        layout.addWidget(self.txt_telefone_celular)
        layout.addWidget(self.lbl_sexo)
        layout.addWidget(self.cb_sexo)
        layout.addWidget(self.lbl_cep)
        layout.addWidget(self.txt_cep)
        layout.addWidget(self.lbl_logradouro)
        layout.addWidget(self.txt_logradouro)
        layout.addWidget(self.lbl_numero)
        layout.addWidget(self.txt_numero)
        layout.addWidget(self.lbl_complemento)
        layout.addWidget(self.txt_complemento)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.txt_bairro)
        layout.addWidget(self.lbl_municipio)
        layout.addWidget(self.txt_municipio)
        layout.addWidget(self.lbl_cep)
        layout.addWidget(self.txt_cep)
        layout.addWidget(self.lbl_estado)
        layout.addWidget(self.txt_estado)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)








