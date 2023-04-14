import datetime


from PySide6.QtWidgets import (QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QMessageBox,
                               QSizePolicy, QVBoxLayout, QTableWidget, QAbstractItemView, QTableWidgetItem, QTextEdit)


from model.Nota import Nota
from controller.nota_dao import DataBase

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(500, 900)
        self.setWindowTitle('Bloco de Notas')

        self.lbl_id = QLabel('ID')
        self.txt_id = QLineEdit()

        self.lbl_titulo = QLabel('Titulo da Nota')
        self.txt_titulo = QLineEdit()

        self.lbl_texto = QLabel('Nota')
        self.txt_texto = QTextEdit()

        self.tabela_notas = QTableWidget()

        self.btn_salvar = QPushButton('Salvar')
        self.btn_remover = QPushButton('Remover')

        self.tabela_notas.setColumnCount(4)
        self.tabela_notas.setHorizontalHeaderLabels(['ID', 'Titulo', 'Texto', 'Data'])
        self.tabela_notas.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela_notas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_id)
        layout.addWidget(self.txt_id)
        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.txt_titulo)
        layout.addWidget(self.lbl_texto)
        layout.addWidget(self.txt_texto)
        layout.addWidget(self.tabela_notas)

        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.btn_remover)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)


        self.lbl_id.setVisible(False)
        self.txt_id.setVisible(False)
        self.btn_remover.setVisible(False)

        self.btn_salvar.clicked.connect(self.salvar_nota)

        # self.btn_remover.clicked.connect(self.remover_cliente)
        #
        # self.txt_cep.editingFinished.connect(self.consultar_endereco)
        # self.tabela_clientes.cellDoubleClicked.connect(self.carregar_dados)
        # self.popular_tabela_cliente()

    def salvar_nota(self):
        db = DataBase()
        retorno = db.consultar_nota(str(self.txt_id.text()))
        id1 = 1
        if retorno is not None:
            id1 = self.txt_titulo.setText(retorno[1]+1)

        nota = Nota(
            id = self.txt_id.setText(str(id1)),
            titulo = self.txt_titulo.text(),
            data = datetime.date.today(),
            texto = self.txt_texto.toPlainText()

        )

        if self.btn_salvar.text() == 'Salvar':
            retorno = db.registrar_nota(nota)
            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Cadastro de Nota ')
                msg.setText('Cadastro realizado com sucesso')
                msg.exec()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao cadastrar ')
                msg.setText('Erro ao cadastrar verfique os dados inseridos')
                msg.exec()

        elif self.btn_salvar.text() == 'Atualizar':
            retorno = db.atualizar_nota(nota)
            if retorno == 'ok':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Nota Atualizada ')
                msg.setText('Nota atualizada com sucesso')
                msg.exec()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Atualizar ')
                msg.setText('Erro ao atualizar verfique os dados inseridos')
                msg.exec()

            #self.popular_tabela_cliente()
            self.txt_id.setReadOnly(False)

    def consulta_nota(self):
        db = DataBase()
        retorno = db.consultar_nota(str(self.txt_id.text()))

        if retorno is not None:
            self.btn_salvar.setText('Atualizar')
            msg = QMessageBox()
            msg.setWindowTitle('Atualizar nota')
            msg.setText(f'A Nota do ID {self.txt_id.text()} poderá ser editada ou excluida')
            msg.exec()

            self.btn_remover.setVisible(True)
            self.lbl_id.setVisible(True)
            self.txt_id.setVisible(True)

            self.txt_texto.setPlainText(retorno[2])
            self.txt_titulo.setText(retorno[3])

