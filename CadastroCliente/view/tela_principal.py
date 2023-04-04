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
        self.lbl_sexo = QLabel('Sexo')
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
        self.btn_limpar.clicked.connect(self.limpar_conteudo)

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

        elif retorno == 'UNIQUE constraint failed: CLIENTE.CPF':

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao cadastrar')
            msg.setText(f'O CPF {self.txt_cpf.text()} já tem cadastro')
            msg.exec()
            cliente_consul = db.consultar_cliente(self.txt_cpf.text())
            self.consultar_conteudo(cliente_consul)


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao cadastrar ')
            msg.setText('Erro ao cadastrar verfique os dados inseridos')
            msg.exec()

    def limpar_conteudo(self):
        self.txt_cpf.setText('')
        self.txt_nome.setText('')
        self.txt_telefone_fixo.setText('')
        self.txt_telefone_celular.setText('')
        self.cb_sexo.setCurrentIndex(0)
        self.txt_cep.setText('')
        self.txt_logradouro.setText('')
        self.txt_numero.setText('')
        self.txt_bairro.setText('')
        self.txt_municipio.setText('')
        self.txt_complemento.setText('')
        self.txt_estado.setText('')

    def consultar_conteudo(self, cliente):
        db = DataBase()

        self.txt_cpf.setText(cliente[0])
        self.txt_nome.setText(cliente[1])
        self.txt_telefone_fixo.setText(cliente[2])
        self.txt_telefone_celular.setText(cliente[3])
        self.cb_sexo.setCurrentText(cliente[4])
        self.txt_cep.setText(cliente[5])
        self.txt_logradouro.setText(cliente[6])
        self.txt_numero.setText(cliente[7])
        self.txt_complemento.setText(cliente[8])
        self.txt_bairro.setText(cliente[9])
        self.txt_municipio.setText(cliente[10])
        self.txt_estado.setText(cliente[11])







