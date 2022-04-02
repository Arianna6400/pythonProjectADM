import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout, QSpacerItem, QSizePolicy, QMessageBox

from PyQt5.QtWidgets import QWidget, QApplication

from listadipendenti.views.VistaListaDipendente import VistaListaDipendente
from listamenu.views.VistaListaMenuAmministratore import VistaListaMenuAmministratore
from listaordinazione.views.VistaListaOrdinazione import VistaListaOrdinazione
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from magazzino.views.VistaMagazzino import VistaMagazzino

#Questa classe definisce la Vista Amministratore, che compare una volta aver effettuato il login correttamente

class VistaHomeAmministratore(QWidget):
    def __init__(self):
        super(VistaHomeAmministratore, self).__init__()

        # Definizione della parte statica, che comprende il font e la dimensione della finestra

        font = QtGui.QFont()
        font.setPointSize(25)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.width = self.screenRect.width()
        self.height = self.screenRect.height()

        # Costruzione del Widget centrale con QtDesigner

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("HomeAmministratore")
        self.centralwidget.setGeometry(QRect(130, 0, 1600, 1000))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 0);\n"
                                         "border-style: outset;\n"
                                         "border-width: 4px;\n"
                                         "border-color: black;\n")

        # Inserimento dello sfondo in background della vista

        self.image = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap('listamenu/data/images/home_pub.jpeg')
        self.image.setPixmap(pixmap)
        self.image.show()
        self.image.setGeometry(QRect(130, 0, 1600, 1000))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Costruzione della griglia principale che contiene i pulsanti

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(350, 400, 1200, 600))
        self.gridLayout = QGridLayout(self.gridLayoutWidget) #Definisce il layout della griglia
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        #Costruzione dei pulsanti che avviano viste specifiche

        self.pushButton_prenotazioni = QPushButton(self.gridLayoutWidget)
        self.pushButton_prenotazioni.setObjectName("pushButton_prenotazioni")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_prenotazioni.sizePolicy().hasHeightForWidth())
        self.pushButton_prenotazioni.setSizePolicy(sizePolicy)
        self.pushButton_prenotazioni.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_prenotazioni.setMinimumHeight(self.height / 10)
        self.pushButton_prenotazioni.setMaximumHeight(self.height / 10)
        self.pushButton_prenotazioni.setStyleSheet("border:2px solid;\n"
                                                    "max-height:48px;\n"
                                                    "border-top-right-radius:20px;\n"
                                                    "border-bottom-left-radius:20px;\n"
                                                    "background-color: rgb(242, 242, 242);\n"
                                                    " color:black;\n"
                                                    " border-style: outset;\n"
                                                    "border-width: 4px;\n"
                                                    "border-color: black;\n"
                                                    "font: 18pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_prenotazioni, 0, 0, 1, 1)

        self.pushButton_quit = QPushButton(self.gridLayoutWidget) #Permette di tornare alla schermata Home
        self.pushButton_quit.setObjectName("pushButton_quit")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        self.pushButton_quit.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_quit.setMinimumHeight(self.height / 10)
        self.pushButton_quit.setMaximumHeight(self.height / 10)
        self.pushButton_quit.setStyleSheet("border:2px solid;\n"
                                            "max-height:48px;\n"
                                            "border-top-right-radius:20px;\n"
                                            "border-bottom-left-radius:20px;\n"
                                            "background-color: rgb(242, 242, 242);\n"
                                            " color:black;\n"
                                            " border-style: outset;\n"
                                            "border-width: 4px;\n"
                                            "border-color: black;\n"
                                            "font: 18pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_quit, 4, 3, 1, 1)

        self.pushButton_menu = QPushButton(self.gridLayoutWidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_menu.setSizePolicy(sizePolicy)
        self.pushButton_menu.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_menu.setMinimumHeight(self.height / 10)
        self.pushButton_menu.setMaximumHeight(self.height / 10)
        self.pushButton_menu.setStyleSheet("border:2px solid;\n"
                                            "max-height:48px;\n"
                                            "border-top-right-radius:20px;\n"
                                            "border-bottom-left-radius:20px;\n"
                                            "background-color: rgb(242, 242, 242);\n"
                                            " color:black;\n"
                                            " border-style: outset;\n"
                                            "border-width: 4px;\n"
                                            "border-color: black;\n"
                                            "font: 18pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_menu, 0, 3, 1, 1)

        self.pushButton_dipendenti = QPushButton(self.gridLayoutWidget)
        self.pushButton_dipendenti.setObjectName("pushButton_dipendenti")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_dipendenti.sizePolicy().hasHeightForWidth())
        self.pushButton_dipendenti.setSizePolicy(sizePolicy)
        self.pushButton_dipendenti.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_dipendenti.setMinimumHeight(self.height / 10)
        self.pushButton_dipendenti.setMaximumHeight(self.height / 10)
        self.pushButton_dipendenti.setStyleSheet("border:2px solid;\n"
                                                "max-height:48px;\n"
                                                "border-top-right-radius:20px;\n"
                                                "border-bottom-left-radius:20px;\n"
                                                "background-color: rgb(242, 242, 242);\n"
                                                " color:black;\n"
                                                " border-style: outset;\n"
                                                "border-width: 4px;\n"
                                                "border-color: black;\n"
                                                "font: 18pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_dipendenti, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 2, 1, 1)

        self.pushButton_magazzino = QPushButton(self.gridLayoutWidget)
        self.pushButton_magazzino.setObjectName("pushButton_magazzino")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_magazzino.sizePolicy().hasHeightForWidth())
        self.pushButton_magazzino.setSizePolicy(sizePolicy)
        self.pushButton_magazzino.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_magazzino.setMinimumHeight(self.height / 10)
        self.pushButton_magazzino.setMaximumHeight(self.height / 10)
        self.pushButton_magazzino.setStyleSheet("border:2px solid;\n"
                                                "max-height:48px;\n"
                                                "border-top-right-radius:20px;\n"
                                                "border-bottom-left-radius:20px;\n"
                                                "background-color: rgb(242, 242, 242);\n"
                                                " color:black;\n"
                                                " border-style: outset;\n"
                                                "border-width: 4px;\n"
                                                "border-color: black;\n"
                                                "font: 18pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_magazzino, 2, 0, 1, 1)

        self.pushButton_ordinazioni = QPushButton(self.gridLayoutWidget)
        self.pushButton_ordinazioni.setObjectName("pushButton_ordinazioni")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ordinazioni.sizePolicy().hasHeightForWidth())
        self.pushButton_ordinazioni.setSizePolicy(sizePolicy)
        self.pushButton_ordinazioni.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_ordinazioni.setMinimumHeight(self.height / 10)
        self.pushButton_ordinazioni.setMaximumHeight(self.height / 10)
        self.pushButton_ordinazioni.setStyleSheet("border:2px solid;\n"
                                                    "max-height:48px;\n"
                                                    "border-top-right-radius:20px;\n"
                                                    "border-bottom-left-radius:20px;\n"
                                                    "background-color: rgb(242, 242, 242);\n"
                                                    " color:black;\n"
                                                    " border-style: outset;\n"
                                                    "border-width: 4px;\n"
                                                    "border-color: black;\n"
                                                    "font: 18pt \\\"Eras Demi ITC\\\";")
        self.gridLayout.addWidget(self.pushButton_ordinazioni, 4, 0, 1, 1)

        #Costruzione della griglia che contiene un label con una scritta e uno con un logo

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(350, 0, 1200, 400))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        pixmap = QPixmap('listamenu/data/images/logo_d.png')
        self.label_2.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setStyleSheet("color: white;\n")
        self.label.setObjectName("label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.setWindowTitle("Home Amministratore")
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #Funzione che connette i pulsanti alle rispettive funzioni
        _translate = QtCore.QCoreApplication.translate

        self.pushButton_prenotazioni.setText(QCoreApplication.translate("HomeAmministratore", "Lista Prenotazioni"))
        self.pushButton_prenotazioni.clicked.connect(self.go_vista_prenotazioni)

        self.pushButton_quit.setText(QCoreApplication.translate("HomeAmministratore", "Home"))
        self.pushButton_quit.clicked.connect(self.go_close)

        self.pushButton_menu.setText(QCoreApplication.translate("HomeAmministratore", "Menu"))
        self.pushButton_menu.clicked.connect(self.go_vista_menu)

        self.pushButton_dipendenti.setText(QCoreApplication.translate("HomeAmministratore", "Lista Dipendenti"))
        self.pushButton_dipendenti.clicked.connect(self.go_vista_dipendenti)

        self.pushButton_magazzino.setText(QCoreApplication.translate("HomeAmministratore", "Magazzino"))
        self.pushButton_magazzino.clicked.connect(self.go_vista_magazzino)

        self.pushButton_ordinazioni.setText(QCoreApplication.translate("HomeAmministratore", "Lista Ordinazioni"))
        self.pushButton_ordinazioni.clicked.connect(self.go_vista_ordinazione)

        self.label.setText(QCoreApplication.translate("HomeAmministratore", "<html>"
                                                                            "<head/>"
                                                                            "<body>"
                                                                            "<p align=\"center\">"
                                                                            "<span style=\" font-size:25pt; font-weight:600;\">Gestione interna:</span>"
                                                                            "</p>"
                                                                            "</body>"
                                                                            "</html>")) #Codice in formato HTML per la scritta del label

    def go_vista_prenotazioni(self): #Funzione che connette alla Vista Prenotazioni
        self.vista_prenotazioni = VistaListaPrenotazioni()
        self.vista_prenotazioni.showMaximized()

    def go_vista_menu(self): #Funzione che connette alla Vista Menu
        self.vista_menu = VistaListaMenuAmministratore()
        self.vista_menu.showMaximized()

    def go_vista_ordinazione(self): #Funzione che connette alla Vista Ordinazione
        self.vista_ordinazione = VistaListaOrdinazione()
        self.vista_ordinazione.showMaximized()

    def go_vista_magazzino(self): #Funzione che connette alla Vista Magazzino
        self.vista_magazzino = VistaMagazzino()
        self.vista_magazzino.showMaximized()

    def go_vista_dipendenti(self): #Funzione che connette alla Vista Dipendenti
        self.vista_dipendenti = VistaListaDipendente()
        self.vista_dipendenti.showMaximized()

    def go_close(self):
        self.close()

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