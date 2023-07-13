import requests
import json
from PySide6.QtWidgets import (QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QMessageBox,
                               QSizePolicy, QVBoxLayout, QTableWidget, QAbstractItemView, QTableWidgetItem)

from infra.repository.cliente_repository import ClienteRepository
from infra.entities.cliente import Cliente


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(500, 900)


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
        self.tabela_clientes = QTableWidget()

        self.tabela_clientes.setColumnCount(12)
        self.tabela_clientes.setHorizontalHeaderLabels(['cpf', 'nome', 'telefone fixo', 'telefone celular',
                                                        'sexo', 'cep', 'logradouro', 'numero', 'complemento',
                                                        'bairro', 'municipio', 'estado'])
        self.tabela_clientes.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)

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
        layout.addWidget(self.tabela_clientes)

        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.btn_limpar)
        layout.addWidget(self.btn_remover)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)


        self.btn_remover.setVisible(False)
        self.btn_salvar.setEnabled(False)
        self.btn_limpar.setVisible(False)


        self.btn_salvar.clicked.connect(self.salvar_cliente)
        self.btn_limpar.clicked.connect(self.limpar_conteudo)
        self.txt_cpf.editingFinished.connect(self.consulta_cliente)
        self.btn_remover.clicked.connect(self.remover_cliente)
        self.txt_cep.editingFinished.connect(self.consultar_endereco)
        self.tabela_clientes.cellDoubleClicked.connect(self.carregar_dados)
        self.popular_tabela_cliente()

        self.txt_cpf.textChanged.connect(self.on_change)
        self.txt_nome.textChanged.connect(self.on_change)

    def on_change(self):

        if self.txt_cpf.text().replace('.','').replace('-','') != '' \
                and self.txt_nome.text() != '':
            self.btn_limpar.setVisible(True)
            self.btn_salvar.setEnabled(True)

        else:
            self.btn_limpar.setVisible(False)
            self.btn_salvar.setEnabled(False)


    def salvar_cliente(self):
        db = ClienteRepository()
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

        if self.btn_salvar.text() == 'Salvar':
            retorno = db.insert(cliente)

            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Cadastro Realizado ')
                msg.setText('Cadastro realizado com sucesso')
                msg.exec()
                self.limpar_conteudo()

            elif retorno == 'UNIQUE constraint failed: CLIENTE.CPF':

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao cadastrar')
                msg.setText(f'O CPF {self.txt_cpf.text()} já tem cadastro')
                msg.exec()


            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao cadastrar ')
                msg.setText('Erro ao cadastrar verfique os dados inseridos')
                msg.exec()
        elif self.btn_salvar.text() == 'Atualizar':

            retorno = db.update(cliente)

            print(f'O retorno é {retorno}')

            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Cadastro Atualizado ')
                msg.setText('Cadastro atualizado com sucesso')
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Atualizar ')
                msg.setText('Erro ao cadastrar verfique os dados inseridos')
                msg.exec()
        self.popular_tabela_cliente()
        self.txt_cpf.setReadOnly(False)
        self.limpar_conteudo()
    def limpar_conteudo(self):
       for widget in self.container.children():
           if isinstance(widget, QLineEdit):
               widget.clear()
           elif isinstance(widget, QMessageBox):
               widget.setCurrentIndex(0)
       self.cb_sexo.setCurrentIndex(0)
       self.btn_remover.setVisible(False)
       self.btn_salvar.setText('Salvar')
       self.txt_cpf.setReadOnly(False)

    def consulta_cliente(self):
        if self.txt_cpf.text().replace('.','').replace('-','') != '':
            db = ClienteRepository()
            retorno = db.select(str(self.txt_cpf.text()))
            print(str(retorno))
            if retorno is not None:
                self.btn_salvar.setText('Atualizar')
                msg = QMessageBox()
                msg.setWindowTitle('Cliente já cadastrado')
                msg.setText(f'O CPF {self.txt_cpf.text()} já tem cadastro')
                msg.exec()
                self.carregar_dados_por_cpf(retorno)

    def remover_cliente(self):
        msg = QMessageBox()
        msg.setWindowTitle('Remover cliente')
        msg.setText('Este cliente será removido')
        msg.setInformativeText(f'Você deseja remover o cliente de CPF {self.txt_cpf.text()}?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.button(QMessageBox.Yes).setText('Sim')
        msg.button(QMessageBox.No).setText('Não')

        resposta = msg.exec()


        if resposta == QMessageBox.Yes:
            db = ClienteRepository()

            if db.delete(self.txt_cpf.text()) == 'ok':
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover cliente')
                nv_msg.setText('Cliente removido com sucesso')
                nv_msg.exec()
                self.limpar_conteudo()
            else:
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover cliente')
                nv_msg.setText('Erro ao Remover')
                nv_msg.exec()

        self.txt_cpf.setReadOnly(False)
        self.btn_salvar.setText('Salvar')
        self.popular_tabela_cliente()


    def consultar_endereco(self):
        url = f'https://viacep.com.br/ws/{str(self.txt_cep.text()).replace(".","").replace("-","")}/json/'
        response = requests.get(url)
        if response.status_code != 400:
            endereco = json.loads(response.text)
            if response.status_code == 200 and 'erro' not in endereco:
                self.txt_logradouro.setText(endereco['logradouro'])
                self.txt_bairro.setText(endereco['bairro'])
                self.txt_municipio.setText(endereco['localidade'])
                self.txt_estado.setText(endereco['uf'])

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Buscar CEP ')
                msg.setText('Erro ao buscar verfique os dados inseridos')
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao Buscar CEP ')
            msg.setText('Erro ao buscar verfique os dados inseridos')
            msg.exec()

    def popular_tabela_cliente(self):
        self.tabela_clientes.setRowCount(0)
        conn = ClienteRepository()
        lista_cliente = conn.select_all()


        self.tabela_clientes.setRowCount(len(lista_cliente))
        linha = 0

        for cliente in lista_cliente:
            valores = [cliente.cpf, cliente.nome, cliente.telefone_fixo,\
                cliente.telefone_celular, cliente.sexo, cliente.cep, \
                cliente.logradouro, cliente.numero, cliente.complemento, \
                cliente.bairro, cliente.municipio, cliente.estado]
            for valor in valores:
                item = QTableWidgetItem(str(valor))
                self.tabela_clientes.setItem(linha, valores.index(valor), item)
                self.tabela_clientes.item(linha, valores.index(valor))
            linha += 1

    def carregar_dados(self, row, column):
        print(row)
        self.txt_cpf.setText(self.tabela_clientes.item(row, 0).text())
        self.txt_nome.setText(self.tabela_clientes.item(row, 1).text())
        self.txt_telefone_fixo.setText(self.tabela_clientes.item(row, 2).text()if self.tabela_clientes.item(row, 2) is not None else '')
        self.txt_telefone_celular.setText(self.tabela_clientes.item(row, 3).text()if self.tabela_clientes.item(row, 3) is not None else '')
        sexo_map = {'não informado': 0, 'Masculino': 1, 'Feminino': 2}
        self.cb_sexo.setCurrentIndex(sexo_map.get(self.tabela_clientes.item(row, 4).text(), 0))
        self.txt_cep.setText(self.tabela_clientes.item(row, 5).text()if self.tabela_clientes.item(row, 5) is not None else '')
        self.txt_logradouro.setText(self.tabela_clientes.item(row, 6).text()if self.tabela_clientes.item(row, 6) is not None else '')
        self.txt_numero.setText(self.tabela_clientes.item(row, 7).text()if self.tabela_clientes.item(row, 7) is not None else '')
        self.txt_complemento.setText(self.tabela_clientes.item(row, 8).text()if self.tabela_clientes.item(row, 8) is not None else '')
        self.txt_bairro.setText(self.tabela_clientes.item(row, 9).text()if self.tabela_clientes.item(row, 9) is not None else '')
        self.txt_municipio.setText(self.tabela_clientes.item(row, 10).text()if self.tabela_clientes.item(row, 10) is not None else '')
        self.txt_estado.setText(self.tabela_clientes.item(row, 11).text()if self.tabela_clientes.item(row, 11) is not None else '')
        self.btn_salvar.setText('Atualizar')
        self.btn_remover.setVisible(True)
        self.txt_cpf.setReadOnly(True)
        self.popular_tabela_cliente()

    def carregar_dados_por_cpf(self, cliente):
        self.txt_nome.setText(cliente.nome)
        self.txt_telefone_fixo.setText(cliente.telefone_fixo)
        self.txt_telefone_celular.setText(cliente.telefone_celular)
        sexo_map = {'não informado': 0, 'Masculino': 1, 'Feminino': 2}
        self.cb_sexo.setCurrentIndex(sexo_map.get(cliente.sexo, 0))
        self.txt_cep.setText(cliente.cep)
        self.txt_logradouro.setText(cliente.logradouro)
        self.txt_numero.setText(cliente.numero)
        self.txt_complemento.setText(cliente.complemento)
        self.txt_bairro.setText(cliente.bairro)
        self.txt_municipio.setText(cliente.municipio)
        self.txt_estado.setText(cliente.estado)
        self.btn_salvar.setText('Atualizar')
        self.btn_remover.setVisible(True)
        self.txt_cpf.setReadOnly(True)
        self.popular_tabela_cliente()


