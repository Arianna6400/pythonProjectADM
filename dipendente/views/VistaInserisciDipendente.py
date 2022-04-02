from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton, QLineEdit, QMessageBox
from dipendente.model.Dipendente import Dipendente

#Questa vista permette l'inserimento delle informazioni di un dipendente da inserire nella Lista Dipendenti

class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback
        self.qlines = {}

        # Definizione della parte statica, che comprende la dimensione della finestra e il colore in background

        self.setWindowTitle('Nuovo Dipendente')
        self.resize(600, 700)
        self.setStyleSheet("background-color: rgb(209, 207, 207);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Definizione della griglia con layout verticale all'interno della quale sono presenti le etichette contenenti le varie informazioni da inserire

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 681))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_info_text("nome", '<font face="Eras Demi ITC"> <font size="10"> Nome: </font>')
        self.add_info_text("cognome", '<font face="Eras Demi ITC"> <font size="10"> Cognome: </font>')
        self.add_info_text("cf", '<font face="Eras Demi ITC"> <font size="10"> Codice fiscale: </font>')
        self.add_info_text("data", '<font face="Eras Demi ITC"> <font size="10"> Data di nascita(dd/mm/yyyy): </font>')
        self.add_info_text("luogo", '<font face="Eras Demi ITC"> <font size="10"> Luogo di nascita: </font>')
        self.add_info_text("telefono", '<font face="Eras Demi ITC"> <font size="10"> Telefono: </font>')
        self.add_info_text("ruolo", '<font face="Eras Demi ITC"> <font size="10"> Ruolo: </font>')

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        #Pulsante di conferma per l'inserimento del nuovo dipendente nella Lista Dipendente

        self.pushButton_ok = QPushButton(self.verticalLayoutWidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_ok.setStyleSheet("border:2px solid;\n"
                                         "max-height:48px;\n"
                                         "border-top-right-radius:20px;\n"
                                         "border-bottom-left-radius:20px;\n"
                                         "background-color: rgb(242, 242, 242);\n"
                                         " color:black;\n"
                                         " border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: black;\n"
                                         "font: 15pt \\\"Eras Demi ITC\\\";")

        self.verticalLayout.addWidget(self.pushButton_ok)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #Funzione che connette il pulsante alla rispettiva funzione
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_ok.setText(QCoreApplication.translate("InserisciDipendente", "Ok"))
        self.pushButton_ok.clicked.connect(self.add_dipendente)

    def add_info_text(self, nome, label): #Funzione che definisce le linee di inserimento del testo e passa il testo alle varie etichette
        self.verticalLayout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        current_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.qlines[nome] = current_text
        self.verticalLayout.addWidget(current_text)

    def add_dipendente(self): #Funzione che controlla l'inserimento e la conferma delle informazioni riguardanti il nuovo dipendente
        for value in self.qlines.values():
            if value.text() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Attenzione!")
                msg.setText(
                    "Per favore, inserisci tutte le informazioni richieste.")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal,
                               QtGui.QIcon.On)
                msg.setWindowIcon(icon)
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.exec_()
                return
        self.controller.aggiungi_dipendente(Dipendente(
            (self.qlines["nome"].text() + self.qlines["cognome"].text()).lower(),
            self.qlines["nome"].text(),
            self.qlines["cognome"].text(),
            self.qlines["data"].text(),
            self.qlines["luogo"].text(),
            self.qlines["cf"].text(),
            self.qlines["telefono"].text(),
            self.qlines["ruolo"].text())
        )
        self.callback()
        self.close()
