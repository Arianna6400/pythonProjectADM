from datetime import datetime, timedelta
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prenotazione.model.Prenotazione import Prenotazione

#Questa vista permette l'inserimento delle informazioni di una prenotazione da inserire nella Lista Prenotazioni

class VistaPrenotazione(QWidget):
    def __init__(self, controller):

        super(VistaPrenotazione, self).__init__()

        self.controller = controller
        self.qlines = []

        # Definizione della parte statica, che comprende la dimensione della finestra e il colore in background

        self.setWindowTitle('Nuova Prenotazione')
        self.resize(600, 700)
        self.setStyleSheet("background-color: rgb(209, 207, 207);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        #Definizione della griglia all'interno della quale sono presenti le etichette per l'inserimento delle informazioni

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 581, 681))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Nome: </font>', 0, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Telefono: </font>', 1, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Numero persone: </font>', 2, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Data (dd/MM/yyyy): </font>', 3, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Ore: </font>', 4, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Minuti: </font>', 5, 0)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(self.verticalSpacer)

        #Pulsante che permette di cofermare l'inserimento della prenotazione

        self.pushButton_ok = QPushButton(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.pushButton_ok, 6, 0)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #Funzione che connette il pulsante alla rispettiva funzione
        _translate = QtCore.QCoreApplication.translate

        self.pushButton_ok.setText(QCoreApplication.translate("InserisciProdotto", "Ok"))
        self.pushButton_ok.clicked.connect(self.add_prenotazione)

    def add_info_text(self, label, gridX, gridY): #Funzione che definisce le linee di inserimento del testo e passa il testo alle varie etichette
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        gridLayout2 = QGridLayout()
        gridLayout2.addWidget(etichetta, 0, 0)
        gridLayout2.addWidget(lineEdit, 1, 0)

        self.gridLayout.addLayout(gridLayout2, gridX, gridY)
        self.qlines.append(lineEdit)

    @staticmethod
    def validate(date_text): #Metodo statico che definisce il format della data da inserire e lancia un errore nel caso di inserimento errato
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def add_prenotazione(self): #Funzione che controlla le informazioni inserite e, se corrette, permette di inserire la prenotazione alla lista
        for value in self.qlines:
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
        if not self.validate(self.qlines[3].text()):
            msg = QMessageBox()
            msg.setWindowTitle("Attenzione!")
            msg.setText(
                "Per favore, inserisci la data nel formato richiesto.")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal,
                           QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
            return
        data = datetime.strptime(self.qlines[3].text(), '%d/%m/%Y')
        new_data1 = data + timedelta(hours=float(self.qlines[4].text()))
        new_data2 = new_data1 + timedelta(minutes=float(self.qlines[5].text()))
        print(new_data2)    # per controllare che la data finale sia corretta, da togliere alla consegna
        self.controller.aggiungi_prenotazione(Prenotazione(self.qlines[0].text(), self.qlines[1].text(), self.qlines[2].text(), new_data2))
        self.close()
