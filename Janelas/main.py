from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

from outra_janela import OutraJanela
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela Principal')
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        self.btn_outra_janela = QPushButton('Abrir outra janela')
        layout.addWidget(self.btn_outra_janela)
        layout.addStretch()
        self.btn_outra_janela.clicked.connect(self.abrir_outra_janela)

    def abrir_outra_janela(self):
        self.hide()
        outra_janela = OutraJanela(self)
        outra_janela.show()


if __name__ == '__main__':
    app = QApplication([])
    main_Window = MainWindow()
    main_Window.show()
    app.exec()