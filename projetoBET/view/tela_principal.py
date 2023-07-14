# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadastroApostas.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QRadioButton, QSizePolicy, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox, QComboBox)
import random
from infra.entities.aposta import Aposta
from infra.repository import aposta_repository


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 874)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 874))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:rgb(93, 93, 93)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_title = QLabel(self.frame_3)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_title)

        self.lbl_nome = QLabel(self.frame_3)
        self.lbl_nome.setObjectName(u"lbl_nome")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.lbl_nome.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setFont(font1)
        self.txt_nome.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.verticalLayout_2.addWidget(self.txt_nome)

        self.frame_aposta_vencedor = QFrame(self.frame_3)
        self.frame_aposta_vencedor.setObjectName(u"frame_aposta_vencedor")
        self.frame_aposta_vencedor.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_aposta_vencedor.setFrameShape(QFrame.StyledPanel)
        self.frame_aposta_vencedor.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_aposta_vencedor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_ap_vencedor = QLabel(self.frame_aposta_vencedor)
        self.lbl_ap_vencedor.setObjectName(u"lbl_ap_vencedor")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.lbl_ap_vencedor.setFont(font2)
        self.lbl_ap_vencedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_ap_vencedor, 0, 0, 1, 2)

        self.comboBox = QComboBox(self.frame_aposta_vencedor)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_aposta_vencedor)

        self.frame_aposta_placar = QFrame(self.frame_3)
        self.frame_aposta_placar.setObjectName(u"frame_aposta_placar")
        self.frame_aposta_placar.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_aposta_placar.setFrameShape(QFrame.StyledPanel)
        self.frame_aposta_placar.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_aposta_placar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_ap_placar = QLabel(self.frame_aposta_placar)
        self.lbl_ap_placar.setObjectName(u"lbl_ap_placar")
        self.lbl_ap_placar.setFont(font2)
        self.lbl_ap_placar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_ap_placar, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_placar_casa = QLabel(self.frame_aposta_placar)
        self.lbl_placar_casa.setObjectName(u"lbl_placar_casa")
        self.lbl_placar_casa.setFont(font2)
        self.lbl_placar_casa.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_placar_casa)

        self.lbl_title_11 = QLabel(self.frame_aposta_placar)
        self.lbl_title_11.setObjectName(u"lbl_title_11")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(26)
        font3.setBold(True)
        self.lbl_title_11.setFont(font3)
        self.lbl_title_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_title_11)

        self.lbl_placar_visitante = QLabel(self.frame_aposta_placar)
        self.lbl_placar_visitante.setObjectName(u"lbl_placar_visitante")
        self.lbl_placar_visitante.setFont(font2)
        self.lbl_placar_visitante.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_placar_visitante)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_apt_casa = QLineEdit(self.frame_aposta_placar)
        self.txt_apt_casa.setObjectName(u"txt_apt_casa")
        self.txt_apt_casa.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.horizontalLayout.addWidget(self.txt_apt_casa)

        self.txt_apt_visitante = QLineEdit(self.frame_aposta_placar)
        self.txt_apt_visitante.setObjectName(u"txt_apt_visitante")
        self.txt_apt_visitante.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.horizontalLayout.addWidget(self.txt_apt_visitante)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_aposta_placar)

        self.frame_qtde_apostas = QFrame(self.frame_3)
        self.frame_qtde_apostas.setObjectName(u"frame_qtde_apostas")
        self.frame_qtde_apostas.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_qtde_apostas.setFrameShape(QFrame.StyledPanel)
        self.frame_qtde_apostas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_qtde_apostas)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_qtde_apostas = QLabel(self.frame_qtde_apostas)
        self.lbl_qtde_apostas.setObjectName(u"lbl_qtde_apostas")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        self.lbl_qtde_apostas.setFont(font4)
        self.lbl_qtde_apostas.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lbl_qtde_apostas)

        self.lbl_valor_qtde_aposta = QLabel(self.frame_qtde_apostas)
        self.lbl_valor_qtde_aposta.setObjectName(u"lbl_valor_qtde_aposta")
        font5 = QFont()
        font5.setPointSize(10)
        self.lbl_valor_qtde_aposta.setFont(font5)
        self.lbl_valor_qtde_aposta.setStyleSheet(u"background-color:rgb(195, 195, 195)")

        self.horizontalLayout_3.addWidget(self.lbl_valor_qtde_aposta)


        self.verticalLayout_2.addWidget(self.frame_qtde_apostas)

        self.frame_valor_aposta = QFrame(self.frame_3)
        self.frame_valor_aposta.setObjectName(u"frame_valor_aposta")
        self.frame_valor_aposta.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_valor_aposta.setFrameShape(QFrame.StyledPanel)
        self.frame_valor_aposta.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_valor_aposta)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.txt_valor_aposta = QLineEdit(self.frame_valor_aposta)
        self.txt_valor_aposta.setObjectName(u"txt_valor_aposta")
        self.txt_valor_aposta.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_7.addWidget(self.txt_valor_aposta, 1, 0, 1, 1)

        self.pb_apostar_2 = QPushButton(self.frame_valor_aposta)
        self.pb_apostar_2.setObjectName(u"pb_apostar_2")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        self.pb_apostar_2.setFont(font6)
        self.pb_apostar_2.setStyleSheet(u"background-color:rgb(16, 100, 255)")

        self.gridLayout_7.addWidget(self.pb_apostar_2, 1, 1, 1, 1)

        self.lbl_valor_aposta = QLabel(self.frame_valor_aposta)
        self.lbl_valor_aposta.setObjectName(u"lbl_valor_aposta")
        self.lbl_valor_aposta.setFont(font2)
        self.lbl_valor_aposta.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lbl_valor_aposta, 0, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_valor_aposta)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_resul_casa = QLabel(self.frame_13)
        self.lbl_resul_casa.setObjectName(u"lbl_resul_casa")
        self.lbl_resul_casa.setFont(font2)
        self.lbl_resul_casa.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_resul_casa, 1, 0, 1, 1)

        self.lbl_title_10 = QLabel(self.frame_13)
        self.lbl_title_10.setObjectName(u"lbl_title_10")
        self.lbl_title_10.setFont(font3)
        self.lbl_title_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_title_10, 1, 1, 1, 1)

        self.lbl_resul_placar = QLabel(self.frame_13)
        self.lbl_resul_placar.setObjectName(u"lbl_resul_placar")
        self.lbl_resul_placar.setFont(font2)
        self.lbl_resul_placar.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_resul_placar, 0, 0, 1, 3)

        self.txt_resul_visitante = QLineEdit(self.frame_13)
        self.txt_resul_visitante.setObjectName(u"txt_resul_visitante")
        self.txt_resul_visitante.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_4.addWidget(self.txt_resul_visitante, 2, 2, 1, 1)

        self.lbl_resul_visitante = QLabel(self.frame_13)
        self.lbl_resul_visitante.setObjectName(u"lbl_resul_visitante")
        self.lbl_resul_visitante.setFont(font2)
        self.lbl_resul_visitante.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_resul_visitante, 1, 2, 1, 1)

        self.txt_resul_casa = QLineEdit(self.frame_13)
        self.txt_resul_casa.setObjectName(u"txt_resul_casa")
        self.txt_resul_casa.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_4.addWidget(self.txt_resul_casa, 2, 0, 1, 1)

        self.pb_gerar_placar = QPushButton(self.frame_13)
        self.pb_gerar_placar.setObjectName(u"pb_gerar_placar")
        self.pb_gerar_placar.setFont(font6)
        self.pb_gerar_placar.setStyleSheet(u"background-color:rgb(16, 100, 255)")

        self.gridLayout_4.addWidget(self.pb_gerar_placar, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.tb_historico = QTableWidget(self.frame_3)
        if (self.tb_historico.columnCount() < 4):
            self.tb_historico.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_historico.setObjectName(u"tb_historico")
        self.tb_historico.setStyleSheet(u"background-color:rgb(195, 195, 195)")

        self.verticalLayout_2.addWidget(self.tb_historico)


        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"APOSTEX", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
#if QT_CONFIG(tooltip)
        self.txt_nome.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txt_nome.setText("")
        self.lbl_ap_vencedor.setText(QCoreApplication.translate("MainWindow", u"APOSTA NO VENCEDOR", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Casa", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Empate", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Visitante", None))

        self.lbl_ap_placar.setText(QCoreApplication.translate("MainWindow", u"APOSTA NO PLACAR", None))
        self.lbl_placar_casa.setText(QCoreApplication.translate("MainWindow", u"CASA", None))
        self.lbl_title_11.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lbl_placar_visitante.setText(QCoreApplication.translate("MainWindow", u"VISITANTE", None))
        self.lbl_qtde_apostas.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE DE APOSTAS", None))
        self.lbl_valor_qtde_aposta.setText("")
        self.pb_apostar_2.setText(QCoreApplication.translate("MainWindow", u"APOSTAR", None))
        self.lbl_valor_aposta.setText(QCoreApplication.translate("MainWindow", u"VALOR DA APOSTA", None))
        self.lbl_resul_casa.setText(QCoreApplication.translate("MainWindow", u"CASA", None))
        self.lbl_title_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lbl_resul_placar.setText(QCoreApplication.translate("MainWindow", u"RESULTADO DO PLACAR", None))
        self.lbl_resul_visitante.setText(QCoreApplication.translate("MainWindow", u"VISITANTE", None))
        self.pb_gerar_placar.setText(QCoreApplication.translate("MainWindow", u"GERAR", None))
        ___qtablewidgetitem = self.tb_historico.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_historico.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tb_historico.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem3 = self.tb_historico.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Valor ganho", None));

        self.pb_apostar_2.clicked.connect(self.verificar_campos)
        self.pb_gerar_placar.clicked.connect(self.gerar_placar)




    # def on_change(self):
    #
    #     if self.tx != '' \
    #             and self.txt_titulo.text() != '':
    #         self.btn_salvar.setEnabled(True)
    #     elif self.txt_texto.toPlainText() != '' \
    #             or self.txt_titulo.text() != '':
    #         self.btn_limpar.setVisible(True)
    #     else:
    #         self.btn_limpar.setVisible(False)
    #         self.btn_salvar.setEnabled(False)

    def verificar_campos(self):
        if not (self.txt_nome.text().split()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro de Aposta')
            msg.setText('Campo Nome é Obrigatório')
            msg.exec()

        elif (self.comboBox.currentIndex()) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro de Aposta')
            msg.setText('Campo Vencedor é Obrigatório')
            msg.exec()

        elif not self.txt_apt_casa.text().strip().isdigit():

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro de Aposta')
            msg.setText('Campo Aposta Casa requer um número inteiro')
            msg.exec()

        elif not self.txt_apt_visitante.text().strip().isdigit():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro de Aposta')
            msg.setText('Campo Aposta Visitante requer um número inteiro')
            msg.exec()

        else:

            valor_aposta_text = self.txt_valor_aposta.text().strip().replace(',', '.')

            if not valor_aposta_text.replace('.', '', 1).isdigit():

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle('Cadastro de Aposta')
                msg.setText('Campo Valor da Aposta requer um número')
                msg.exec()

            else:

                valor_aposta = float(valor_aposta_text)
                if valor_aposta <= 0:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Cadastro de Aposta')
                    msg.setText('Campo Valor da Aposta deve ser maior que zero')
                    msg.exec()

                else:
                    self.salvar_aposta()

    def salvar_aposta(self):

        db = aposta_repository.ApostaRepository()
        aposta = Aposta(
            nome = self.txt_nome.text(),
            aposta_vencedor = self.comboBox.currentIndex(),
            placar_casa= self.txt_apt_casa.text(),
            placar_visitante= self.txt_apt_visitante.text(),
            valor_aposta = float(self.txt_valor_aposta.text().strip().replace(',', '.')),
        )

        retorno = db.insert(aposta)

        if retorno == 'ok':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('Cadastro Realizado ')
            msg.setText('Cadastro realizado com sucesso')
            msg.exec()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao cadastrar ')
            msg.setText('Erro ao cadastrar verfique os dados inseridos')
            msg.exec()


    def gerar_placar(self):
        db = aposta_repository.ApostaRepository()

        retorno = db.select_all()
        print(retorno)
        if len(retorno) > 0:
            self.txt_resul_casa.setText(str(random.randint(0, 10)))
            self.txt_resul_visitante.setText(str(random.randint(0, 10)))
            self.popular_tb()


    def validar_vencedor(placar):
        if placar[0]['gols'] > placar[1]['gols']:
            return placar[0]['time']
        elif placar[1]['gols'] > placar[0]['gols']:
            return placar[1]['time']
        else:
            return "Empate"


        placar = gerar_placar()
        exibir_placar(placar)

        ganhador = validar_vencedor(placar)
        print(f"Vencedor: {ganhador} ganhou")

    def popular_tb(self):
        db = aposta_repository.ApostaRepository()
        retorno = db.select_all()
        ganhadores = []
        vencedor = None
        if int(self.txt_resul_casa.text()) > int(self.txt_resul_visitante.text()):
            vencedor = 1
        elif int(self.txt_resul_casa.text()) == int(self.txt_resul_visitante.text()):
            vencedor = 2
        else:
            vencedor = 3
        for resultado in retorno:
            if int(resultado.aposta_vencedor) == vencedor:
                ganhadores.append(resultado)


        self.tb_historico.setRowCount(len(ganhadores))

        for linha, aposta in enumerate(ganhadores):
            valores = [aposta.id, aposta.nome, aposta.valor_aposta]
            for coluna, valor in enumerate(valores):
                item = QTableWidgetItem(str(valor))
                self.tb_historico.setItem(linha, coluna, item)