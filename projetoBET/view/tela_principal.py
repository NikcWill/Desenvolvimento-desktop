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
    QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox)

from infra.entities.aposta import Aposta
from infra.repository import aposta_repository


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(523, 874)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 874))
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color:rgb(93, 93, 93)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_title = QLabel(self.frame_3)
        self.lbl_title.setObjectName(u"lbl_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_title)

        self.lbl_nome = QLabel(self.frame_3)
        self.lbl_nome.setObjectName(u"lbl_nome")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.lbl_nome.setFont(font1)

        self.verticalLayout.addWidget(self.lbl_nome)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setFont(font1)
        self.txt_nome.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.verticalLayout.addWidget(self.txt_nome)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb_casa = QRadioButton(self.frame_12)
        self.rb_casa.setObjectName(u"rb_casa")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.rb_casa.setFont(font2)
        self.rb_casa.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_2.addWidget(self.rb_casa, 1, 0, 1, 1)

        self.rb_visitante = QRadioButton(self.frame_12)
        self.rb_visitante.setObjectName(u"rb_visitante")
        self.rb_visitante.setFont(font2)
        self.rb_visitante.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_2.addWidget(self.rb_visitante, 1, 1, 1, 1)

        self.lbl_ap_vencedor = QLabel(self.frame_12)
        self.lbl_ap_vencedor.setObjectName(u"lbl_ap_vencedor")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(False)
        self.lbl_ap_vencedor.setFont(font3)
        self.lbl_ap_vencedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_ap_vencedor, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_ap_placar = QLabel(self.frame_8)
        self.lbl_ap_placar.setObjectName(u"lbl_ap_placar")
        self.lbl_ap_placar.setFont(font3)
        self.lbl_ap_placar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_ap_placar, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_placar_casa = QLabel(self.frame_8)
        self.lbl_placar_casa.setObjectName(u"lbl_placar_casa")
        self.lbl_placar_casa.setFont(font3)
        self.lbl_placar_casa.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_placar_casa)

        self.lbl_title_11 = QLabel(self.frame_8)
        self.lbl_title_11.setObjectName(u"lbl_title_11")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(26)
        font4.setBold(True)
        self.lbl_title_11.setFont(font4)
        self.lbl_title_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_title_11)

        self.lbl_placar_visitante = QLabel(self.frame_8)
        self.lbl_placar_visitante.setObjectName(u"lbl_placar_visitante")
        self.lbl_placar_visitante.setFont(font3)
        self.lbl_placar_visitante.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_placar_visitante)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_apt_casa = QLineEdit(self.frame_8)
        self.txt_apt_casa.setObjectName(u"txt_apt_casa")
        self.txt_apt_casa.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.horizontalLayout.addWidget(self.txt_apt_casa)

        self.txt_apt_visitante = QLineEdit(self.frame_8)
        self.txt_apt_visitante.setObjectName(u"txt_apt_visitante")
        self.txt_apt_visitante.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.horizontalLayout.addWidget(self.txt_apt_visitante)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txt_valor_aposta = QLineEdit(self.frame_16)
        self.txt_valor_aposta.setObjectName(u"txt_valor_aposta")
        self.txt_valor_aposta.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_5.addWidget(self.txt_valor_aposta, 1, 0, 1, 1)

        self.pb_apostar = QPushButton(self.frame_16)
        self.pb_apostar.setObjectName(u"pb_apostar")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.pb_apostar.setFont(font5)
        self.pb_apostar.setStyleSheet(u"background-color:rgb(16, 100, 255)")

        self.gridLayout_5.addWidget(self.pb_apostar, 1, 1, 1, 1)

        self.lbl_valor_aposta = QLabel(self.frame_16)
        self.lbl_valor_aposta.setObjectName(u"lbl_valor_aposta")
        self.lbl_valor_aposta.setFont(font3)
        self.lbl_valor_aposta.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lbl_valor_aposta, 0, 0, 1, 2)


        self.verticalLayout.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color:rgb(195, 195, 195)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_13)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_resul_visitante = QLineEdit(self.frame_13)
        self.txt_resul_visitante.setObjectName(u"txt_resul_visitante")
        self.txt_resul_visitante.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_4.addWidget(self.txt_resul_visitante, 2, 2, 1, 1)

        self.txt_resul_casa = QLineEdit(self.frame_13)
        self.txt_resul_casa.setObjectName(u"txt_resul_casa")
        self.txt_resul_casa.setStyleSheet(u"background-color:rgb(253, 253, 253)")

        self.gridLayout_4.addWidget(self.txt_resul_casa, 2, 0, 1, 1)

        self.lbl_resul_visitante = QLabel(self.frame_13)
        self.lbl_resul_visitante.setObjectName(u"lbl_resul_visitante")
        self.lbl_resul_visitante.setFont(font3)
        self.lbl_resul_visitante.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_resul_visitante, 1, 2, 1, 1)

        self.lbl_resul_placar = QLabel(self.frame_13)
        self.lbl_resul_placar.setObjectName(u"lbl_resul_placar")
        self.lbl_resul_placar.setFont(font3)
        self.lbl_resul_placar.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_resul_placar, 0, 0, 1, 3)

        self.lbl_resul_casa = QLabel(self.frame_13)
        self.lbl_resul_casa.setObjectName(u"lbl_resul_casa")
        self.lbl_resul_casa.setFont(font3)
        self.lbl_resul_casa.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_resul_casa, 1, 0, 1, 1)

        self.lbl_title_10 = QLabel(self.frame_13)
        self.lbl_title_10.setObjectName(u"lbl_title_10")
        self.lbl_title_10.setFont(font4)
        self.lbl_title_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbl_title_10, 1, 1, 1, 1)

        self.pb_gerar_placar = QPushButton(self.frame_13)
        self.pb_gerar_placar.setObjectName(u"pb_gerar_placar")
        self.pb_gerar_placar.setFont(font5)
        self.pb_gerar_placar.setStyleSheet(u"background-color:rgb(16, 100, 255)")

        self.gridLayout_4.addWidget(self.pb_gerar_placar, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_13)

        self.tb_historico = QTableWidget(self.frame_3)
        if (self.tb_historico.columnCount() < 3):
            self.tb_historico.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_historico.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_historico.setObjectName(u"tb_historico")
        self.tb_historico.setStyleSheet(u"background-color:rgb(195, 195, 195)")

        self.verticalLayout.addWidget(self.tb_historico)


        self.gridLayout_6.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

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
        self.rb_casa.setText(QCoreApplication.translate("MainWindow", u"Casa", None))
        self.rb_visitante.setText(QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.lbl_ap_vencedor.setText(QCoreApplication.translate("MainWindow", u"APOSTA NO VENCEDOR", None))
        self.lbl_ap_placar.setText(QCoreApplication.translate("MainWindow", u"APOSTA NO PLACAR", None))
        self.lbl_placar_casa.setText(QCoreApplication.translate("MainWindow", u"CASA", None))
        self.lbl_title_11.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lbl_placar_visitante.setText(QCoreApplication.translate("MainWindow", u"VISITANTE", None))
        self.pb_apostar.setText(QCoreApplication.translate("MainWindow", u"APOSTAR", None))
        self.lbl_valor_aposta.setText(QCoreApplication.translate("MainWindow", u"VALOR DA APOSTA", None))
        self.lbl_resul_visitante.setText(QCoreApplication.translate("MainWindow", u"VISITANTE", None))
        self.lbl_resul_placar.setText(QCoreApplication.translate("MainWindow", u"RESULTADO DO PLACAR", None))
        self.lbl_resul_casa.setText(QCoreApplication.translate("MainWindow", u"CASA", None))
        self.lbl_title_10.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pb_gerar_placar.setText(QCoreApplication.translate("MainWindow", u"GERAR", None))
        ___qtablewidgetitem = self.tb_historico.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_historico.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aposta", None));
        ___qtablewidgetitem2 = self.tb_historico.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor ganho", None));
    # retranslateUi

        self.pb_apostar.clicked.connect(self.salvar_aposta)

    def salvar_aposta(self):
        db = aposta_repository.ApostaRepository
        aposta = Aposta(
            nome = self.txt_nome.text(),
            aposta_vencedor = self.rb_casa.text(),
            placar_casa= self.txt_apt_casa.text(),
            placar_visitante= self.txt_apt_visitante.text(),
            valor_aposta = self.txt_valor_aposta.text(),
        )
        print(aposta)
        retorno = db.insert(aposta)
        print(retorno)
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


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Erro ao cadastrar ')
            msg.setText('Erro ao cadastrar verfique os dados inseridos')
            msg.exec()


