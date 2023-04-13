
from PySide6.QtWidgets import (QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QWidget, QMessageBox,
                               QSizePolicy, QVBoxLayout, QTableWidget, QAbstractItemView, QTableWidgetItem)


from BlocoDeNotas.model.nota import Nota
from BlocoDeNotas.controller.nota_dao import DataBase

class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(500, 900)


        self.setWindowTitle('Bloco de Notas')

        self.lbl_id = QLabel('ID')
        self.txt_id = QLineEdit()
        self.lbl_titulo = QLabel('Titulo da Nota')
        self.txt_titulo = QLineEdit()
        self.lbl_nota = QLabel('Nota')
        self.txt_nota = QLineEdit().setMinimumSize(200, 50)
        self.tabela_notas = QTableWidget()

        self.btn_salvar = QPushButton('Salvar')
        self.btn_limpar = QPushButton('Limpar')
        self.btn_remover = QPushButton('Remover')

        self.tabela_notas.setColumnCount(12)
        self.tabela_notas.setHorizontalHeaderLabels(['ID', 'Titulo', 'Texto', 'Data'])
        self.tabela_notas.setSelectionMode(QAbstractItemView.NoSelection)
        self.tabela_notas.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_id)
        layout.addWidget(self.txt_id)
        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.txt_titulo)
        layout.addWidget(self.lbl_nota)
        layout.addWidget(self.txt_nota)
        layout.addWidget(self.tabela_notas)

        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.btn_limpar)
        layout.addWidget(self.btn_remover)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)