import datetime

from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QMessageBox,
                               QSizePolicy, QVBoxLayout, QTableWidget, QAbstractItemView, QTableWidgetItem, QTextEdit,
                               QHeaderView)

from infra.repository.nota_repository import NotaRepository
from infra.entities.nota import Nota

from infra.configs.connection import DBConnectionHandler

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        conn = DBConnectionHandler()

        self.setMinimumSize(500, 900)
        self.setWindowTitle('Bloco de Notas')

        self.lbl_id = QLabel('ID')
        self.txt_id = QLineEdit()

        self.lbl_titulo = QLabel('Titulo da Nota')
        self.txt_titulo = QLineEdit()

        self.lbl_texto = QLabel('Nota')
        self.txt_texto = QTextEdit()

        self.txt_data = datetime.date

        self.tabela_notas = QTableWidget()

        self.btn_salvar = QPushButton('Salvar')
        self.btn_remover = QPushButton('Remover')
        self.btn_limpar = QPushButton('Limpar')

        self.tabela_notas.setColumnCount(4)
        self.tabela_notas.setHorizontalHeaderLabels(['ID', 'Titulo', 'Texto', 'Data'])
        self.tabela_notas.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela_notas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tabela_notas.setColumnWidth(0, 10)
        self.tabela_notas.setColumnWidth(1, 145)
        self.tabela_notas.setColumnWidth(2, 200)
        self.tabela_notas.setColumnWidth(3, 80)

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
        layout.addWidget(self.btn_limpar)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)

        self.lbl_id.setVisible(False)
        self.txt_id.setVisible(False)
        self.btn_remover.setVisible(False)
        self.btn_salvar.setEnabled(False)
        self.btn_limpar.setVisible(False)

        self.btn_salvar.clicked.connect(self.salvar_nota)
        self.btn_limpar.clicked.connect(self.limpar_conteudo)
        self.btn_remover.clicked.connect(self.remover_nota)
        self.tabela_notas.cellDoubleClicked.connect(self.carregar_dados)
        self.popular_tabela_notas()

        self.txt_titulo.textChanged.connect(self.on_change)
        self.txt_texto.textChanged.connect(self.on_change)

    def on_change(self):

        if self.txt_texto.toPlainText() != '' \
                or self.txt_titulo.text() != '':
            self.btn_limpar.setVisible(True)
            self.btn_salvar.setEnabled(True)

        else:
            self.btn_limpar.setVisible(False)
            self.btn_salvar.setEnabled(False)

    def salvar_nota(self):
        db = NotaRepository()
        nota = Nota(

            titulo = self.txt_titulo.text(),
            data = datetime.date.today().strftime('%d/%m/%y'),
            texto = self.txt_texto.toPlainText()
        )

        if self.btn_salvar.text() == 'Salvar':
            retorno = db.insert(nota)
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
                self.popular_tabela_notas()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle('Erro ao Atualizar ')
                msg.setText('Erro ao atualizar verfique os dados inseridos')
                msg.exec()

        self.popular_tabela_notas()

    def consulta_nota(self):
        db = DataBase()
        retorno = db.consultar_nota(str(self.txt_id.text()))

        if retorno is not None:
            self.btn_salvar.setText('Atualizar')
            msg = QMessageBox()
            msg.setWindowTitle('Atualizar nota')
            msg.setText(f'A Nota do ID {self.txt_id.text()} poderá ser editada ou excluida')
            msg.exec()

            self.txt_texto.setPlainText(retorno[2])
            self.txt_titulo.setText(retorno[3])

    def popular_tabela_notas(self):
        self.tabela_notas.setRowCount(0)
        conn = NotaRepository()
        lista_notas = conn.select_all()
        self.tabela_notas.setRowCount(len(lista_notas))

        linha = 0

        for nota in lista_notas:
            valores = [nota.id, nota.titulo, nota.texto, nota.data]
            for valor in valores:
                item = QTableWidgetItem(str(valor))
                fonte = QFont('Arial', 10)
                self.tabela_notas.setItem(linha, valores.index(valor), item)
                self.tabela_notas.item(linha, valores.index(valor))
            linha+=1


    def carregar_dados(self, row, column):
        self.txt_id.setText(self.tabela_notas.item(row, 0).text())
        self.txt_titulo.setText(self.tabela_notas.item(row, 1).text())
        self.txt_texto.setText(self.tabela_notas.item(row, 2).text())

        self.btn_salvar.setText('Atualizar')
        self.btn_remover.setVisible(True)
        self.txt_id.setReadOnly(True)

        self.lbl_id.setVisible(True)
        self.txt_id.setVisible(True)

        self.popular_tabela_notas()
    def limpar_conteudo(self):
        for widget in self.container.children():
            if isinstance(widget, QLineEdit):
                widget.clear()
            elif isinstance(widget, QTextEdit):
                widget.clear()
            elif isinstance(widget, QMessageBox):
                widget.setCurrentIndex(0)
        self.lbl_id.setVisible(False)
        self.txt_id.setVisible(False)
        self.btn_remover.setVisible(False)
        self.btn_salvar.setText('Salvar')
    def remover_nota(self):
        msg = QMessageBox()
        msg.setWindowTitle('Remover Nota')
        msg.setText('Esta nota será removida')
        msg.setInformativeText(f'Você deseja remover a nota {self.txt_id.text()}?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.button(QMessageBox.Yes).setText('Sim')
        msg.button(QMessageBox.No).setText('Não')

        resposta = msg.exec()

        if resposta == QMessageBox.Yes:
            db = DataBase()

            if db.deletar_nota(self.txt_id.text()) == 'ok':
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover nota')
                nv_msg.setText('Nota removida com sucesso')
                nv_msg.exec()
            else:
                nv_msg = QMessageBox()
                nv_msg.setWindowTitle('Remover nota')
                nv_msg.setText('Erro ao Remover')
                nv_msg.exec()
            self.txt_id.setReadOnly(False)
            self.btn_salvar.setText('Salvar')
            self.popular_tabela_notas()
            self.limpar_conteudo()

