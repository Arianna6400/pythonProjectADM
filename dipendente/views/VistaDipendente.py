from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controller.ControlloreDipendente import ControlloreDipendente

#Questa vista permette la visualizzazione delle informazioni di un dipendente presente nella Lista Dipendenti

class VistaDipendente(QWidget):
    def __init__(self, dipendente, controllore, callback):
        super(VistaDipendente, self).__init__()
        self.controller = ControlloreDipendente(dipendente)
        self.controllore = controllore
        self.callback = callback

        # Definizione della parte statica, che comprende la dimensione della finestra e il colore in background

        self.setWindowTitle('Vista Dipendente')
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb(209, 207, 207);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        #Definizione della griglia con layout verticale all'interno della quale sono presenti le etichette contenenti le varie informazioni

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.verticalLayoutWidget) #Label in cima nel quale è stampato il nome e cognome del dipendente
        self.label_name.setObjectName("label_name")
        self.label_name.setStyleSheet("font: 24pt \"Eras Demi ITC\";")

        self.verticalLayout.addWidget(self.label_name)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout.addItem(self.verticalSpacer)

        #Definizione con codice in formato HTML delle etichette contenenti le informazioni del dipendente

        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Nome: {}</span></p></body></html>".format(self.controller.get_nome_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Cognome: {}</span></p></body></html>".format(self.controller.get_cognome_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Codice Fiscale: {}</span></p></body></html>".format(self.controller.get_cf_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Data Nascita: {}</span></p></body></html>".format(self.controller.get_data_nascita_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Luogo Nascita: {}</span></p></body></html>".format(self.controller.get_luogo_nascita_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Telefono: {}</span></p></body></html>".format(self.controller.get_telefono_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-style:italic;\">Ruolo: {}</span></p></body></html>".format(self.controller.get_ruolo_dipendente())))

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout.addItem(self.verticalSpacer_2)

        #Pulsante contenuto nella griglia che permette di eliminare le informazioni del dipendente che si sta visualizzando, eliminandolo dalla Lista Dipendente

        self.pushButton_delete = QPushButton(self.verticalLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setStyleSheet("border:2px solid;\n"
                                             "max-height:48px;\n"
                                             "border-top-right-radius:20px;\n"
                                             "border-bottom-left-radius:20px;\n"
                                             "background-color: rgb(242, 242, 242);\n"
                                             " color:black;\n"
                                             " border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: black;\n"
                                             "font: 15pt \\\"Eras Demi ITC\\\";")

        self.verticalLayout.addWidget(self.pushButton_delete)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #Funzione che connette il pulsante alla rispettiva funzione, e che passa al label d'intestazione il nome e cognome del dipendente
        _translate = QtCore.QCoreApplication.translate
        self.label_name.setText(QCoreApplication.translate("Form", self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente()))
        self.pushButton_delete.setText(QCoreApplication.translate("Form", "Elimina"))
        self.pushButton_delete.clicked.connect(self.elimina_dipendente)

    def get_info(self, text): #Funzione che passa le informazioni alle etichette
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente(self): #Funzione che permette la cancellazione delle informazioni del dipendente
        self.controllore.elimina_dipendente_by_id(self.controller.get_id_dipendente())
        self.callback()
        self.close()
