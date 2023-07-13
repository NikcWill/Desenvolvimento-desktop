from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class OutraJanela(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Outra Janela')

        central_widget = QWidget(self)

        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.btn_voltar = QPushButton('Voltar principal', self)
        layout.addWidget(self.btn_voltar)
        layout.addStretch()
        self.btn_voltar.clicked.connect(self.fechar_janela)
    def fechar_janela(self):
        self.parent().show()
        self.close()