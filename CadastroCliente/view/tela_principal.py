import requests
import json
from PySide6.QtWidgets import (QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QMessageBox,
                               QSizePolicy, QVBoxLayout)

from CadastroCliente.model.cliente import Cliente
from CadastroCliente.controller.cliente_dao import DataBase



class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 300)


        self.setWindowTitle('Cadastro de cliente')

        self.lbl_sexo = QLabel('Sexo')
        self.lbl_cpf = QLabel('CPF')
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask('000.000.000-00')
        self.lbl_nome = QLabel('Nome')
        self.txt_nome = QLineEdit()
        self.lbl_telefone_fixo = QLabel('Telefone Fixo')
        self.txt_telefone_fixo = QLineEdit()
        self.txt_telefone_fixo.setInputMask('(00)0000-0000')
        self.lbl_telefone_celular = QLabel('Telefone Celular')
        self.txt_telefone_celular = QLineEdit()
        self.txt_telefone_celular.setInputMask('(00)00000-0000')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['não imformado', 'Masculino', 'Feminino'])
        self.lbl_cep = QLabel('CEP')
        self.txt_cep = QLineEdit()
        self.lbl_logradouro = QLabel('Logradouro')
        self.txt_logradouro = QLineEdit()
        self.lbl_numero = QLabel('Numero')
        self.txt_numero = QLineEdit()
        self.lbl_bairro = QLabel('Bairro')
        self.txt_bairro = QLineEdit()
        self.lbl_municipio = QLabel('Municipio')
        self.txt_municipio = QLineEdit()
        self.lbl_complemento = QLabel('Complemento')
        self.txt_complemento = QLineEdit()
        self.lbl_estado = QLabel('Estado')
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
        layout.addWidget(self.lbl_estado)
        layout.addWidget(self.txt_estado)

        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.btn_limpar)
        layout.addWidget(self.btn_remover)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)

        self.btn_remover.setVisible(False)
        self.btn_salvar.clicked.connect(self.salvar_cliente)
    def salvar_cliente(self):
        db = DataBase()

        cliente = Cliente(
            cpf = self.txt_cpf.text(),
            nome = self.txt_nome.text(),
            telefone_fixo = self.txt_telefone_fixo.text(),
            telefone_celular = self.txt_telefone_celular.text(),
            sexo = self.cb_sexo.currentText(),
            cep = self.txt_cep.text(),
            logradouro=self.txt_logradouro.text(),
            numero=self.txt_numero.text(),
            complemento=self.txt_complemento.text(),
            bairro=self.txt_bairro.text(),
            municipio=self.txt_municipio.text(),
            estado=self.txt_estado.text()
        )
        retorno = db.registrar_cliente(cliente)

        if retorno == 'ok':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro Realizado ')
            msg.setText('Cadastro realizado com sucesso')
            msg.exec()
        elif 'UNIQUE constraint failed: ' in retorno[0]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao cadastrar')
            msg.setText(f'O CPF {self.txt_cpf} já tem cadastro')
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao cadastrar ')
            msg.setText('Erro ao cadastrar verfique os dados inseridos')
            msg.exec()

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






