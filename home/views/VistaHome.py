import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QRect, QCoreApplication, QTimer, QTime
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QSplashScreen, QApplication, QPushButton, \
    QSpacerItem, QSizePolicy, QHBoxLayout
import time

from homeamministratore.views.LoginAmministratore import LoginAmministratore
from homecliente.views.LoginCliente import LoginCliente


# Questa classe definisce la vista Home iniziale del software che compare all'accensione

class VistaHome(QWidget):
    def __init__(self):
        super(VistaHome, self).__init__()

        # Definizione della parte statica, che comprende il font e la dimensione della finestra

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        # Icona che parte all'accensione dell'applicazione

        avvio_icon = QSplashScreen()
        avvio_icon.setPixmap(QPixmap('listamenu/data/images/logo_donegal.png'))
        avvio_icon.show()
        time.sleep(2)

        # Costruzione del Widget centrale con QtDesigner

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("Home")
        self.centralwidget.setGeometry(QRect(130, 0, 1600, 1000))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 4px;\n"
                                         "border-color: black;\n")

        # Inserimento dello sfondo in background della vista

        self.image = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('listamenu/data/images/pub.jpeg')
        self.image.setPixmap(pixmap)
        self.image.show()
        self.image.setGeometry(QRect(130, 0, 1600, 1000))

        # Icona della finestra (uguale in ogni altra vista)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Costruzione della griglia principale che contiene i pulsanti

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(300, 300, 1200, 800))
        self.horizontalLayout = QHBoxLayout(self.gridLayoutWidget)  # Definisce il layout della griglia
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # Costruzione dei pulsanti che avviano le schermate di login per le rispettive interfacce

        self.pushButton_amministratore = QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_amministratore.sizePolicy().hasHeightForWidth())
        self.pushButton_amministratore.setSizePolicy(sizePolicy)
        self.pushButton_amministratore.setMinimumSize(QtCore.QSize(130, 60))
        self.pushButton_amministratore.setMinimumHeight(self.height / 5)
        self.pushButton_amministratore.setMaximumHeight(self.height / 5)
        self.pushButton_amministratore.setObjectName("pushButton_amministratore")
        self.pushButton_amministratore.setStyleSheet("border:2px solid;\n"
                                                     "max-height:48px;\n"
                                                     "border-top-right-radius:20px;\n"
                                                     "border-bottom-left-radius:20px;\n"
                                                     "background-color: rgb(242, 242, 242);\n"
                                                     "color:black;\n"
                                                     "border-style: outset;\n"
                                                     "border-width: 4px;\n"
                                                     "border-color: black;\n"
                                                     "font: 18pt \\\"Eras Demi ITC\\\";")

        self.horizontalLayout.addWidget(self.pushButton_amministratore)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_cliente = QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cliente.sizePolicy().hasHeightForWidth())
        self.pushButton_cliente.setSizePolicy(sizePolicy)
        self.pushButton_cliente.setMinimumSize(QtCore.QSize(130, 60))
        self.pushButton_cliente.setMinimumHeight(self.height / 5)
        self.pushButton_cliente.setMaximumHeight(self.height / 5)
        self.pushButton_cliente.setObjectName("pushButton_cliente")
        self.pushButton_cliente.setStyleSheet("border:2px solid;\n"
                                              "max-height:48px;\n"
                                              "border-top-right-radius:20px;\n"
                                              "border-bottom-left-radius:20px;\n"
                                              "background-color: rgb(242, 242, 242);\n"
                                              "color:black;\n"
                                              "border-style: outset;\n"
                                              "border-width: 4px;\n"
                                              "border-color: black;\n"
                                              "font: 18pt \\\"Eras Demi ITC\\\";")
        self.horizontalLayout.addWidget(self.pushButton_cliente)

        # Costruzione della griglia contenente il Label con scritta 'Welcome' e l'orologio

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(300, 0, 1800, 450))
        self.horizontalLayout_2 = QHBoxLayout(self.gridLayoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        pixmap = QPixmap('listamenu/data/images/logo_welcome.png')
        self.label.setPixmap(pixmap)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        font_clock = QFont('Eras Demi ITC', 40, QFont.Bold)
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setFont(font_clock)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        # Definizione dell'orologio
        timer = QTimer(self)
        timer.timeout.connect(self.mostra_ora)
        timer.start(1000)
        self.mostra_ora()

        self.setWindowTitle("Home")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):  # Funzione che connette i pulsanti alle rispettive funzioni
        _translate = QtCore.QCoreApplication.translate

        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_amministratore.setText(QCoreApplication.translate("Home", "Amministratore"))
        self.pushButton_amministratore.clicked.connect(self.go_login_amministratore)
        self.pushButton_cliente.setText(QCoreApplication.translate("Home", "Cliente"))
        self.pushButton_cliente.clicked.connect(self.go_login_cliente)

    def mostra_ora(self):  # Funzione che setta l'orologio a orario corrente
        currentTime = QTime.currentTime()
        display_text = currentTime.toString("hh:mm:ss")
        self.label_2.setText(display_text)

    def go_login_amministratore(self):  # Funzione che connette il pulsante Amministratore alla sua schermata di login
        self.login_amministratore = LoginAmministratore()
        self.login_amministratore.show()

    def go_login_cliente(self):  # Funzione che connette il pulsante Cliente alla sua schermata di login
        self.login_cliente = LoginCliente()
        self.login_cliente.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Attenzione!',
                                     'Vuoi chiudere il programma?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            if not type(event) == bool:
                event.ignore()
