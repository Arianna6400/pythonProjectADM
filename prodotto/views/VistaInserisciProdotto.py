from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy, QPushButton, QLineEdit, QMessageBox, \
    QGridLayout

from prodotto.model.ProdottoSingolo import ProdottoSingolo

#Questa vista permette l'inserimento delle informazioni di un prodotto da inserire nel Menu

class VistaInserisciProdotto(QWidget):

    def __init__(self, controller, callback):

        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        self.callback = callback
        self.last = 3
        self.ingredienti = {}
        self.temp = ""
        self.key = []
        self.qlines = {}
        self.alimenti = {}

        # Definizione della parte statica, che comprende la dimensione della finestra e il colore in background

        self.setWindowTitle('Aggiungi Nuovo Prodotto')
        self.resize(600, 700)
        self.setStyleSheet("background-color: rgb(209, 207, 207);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        #Definizione della griglia all'interno della quale sono presenti le etichette contenenti le varie informazioni da inserire

        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 581, 681))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.add_info_text("prodotto", '<font face="Eras Demi ITC"> <font size="10"> Prodotto: </font>', 0, 0)
        self.add_info_text("prezzo", '<font face="Eras Demi ITC"> <font size="10"> Prezzo: </font>', 1, 0)
        self.add_info_ingredienti('<font face="Eras Demi ITC"> <font size="10"> Ingredienti: </font>', 2, 0, True)
        self.add_info_ingredienti('<font face="Eras Demi ITC"> <font size="10"> Quantità: </font>', 2, 1, False)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(self.verticalSpacer)

        #Pulsante che permette di aggiungere una nuova linea se necessario per un ingrediente in più

        self.pushButton_plus = QPushButton(self.gridLayoutWidget)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_plus.setStyleSheet("border:2px solid;\n"
                                         "max-height:48px;\n"
                                         "border-top-right-radius:20px;\n"
                                         "border-bottom-left-radius:20px;\n"
                                         "background-color: rgb(242, 242, 242);\n"
                                         " color:black;\n"
                                         " border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: black;\n"
                                         "font: 13pt \\\"Eras Demi ITC\\\";")

        self.gridLayout.addWidget(self.pushButton_plus, self.last, 0)

        #Pulsante per la conferma dell'inserimento del nuovo prodotto

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
                                         "font: 13pt \\\"Eras Demi ITC\\\";")

        self.gridLayout.addWidget(self.pushButton_ok, self.last, 1)

        # Definizone della barra di scorrimento laterale

        self.scrollbar = QtWidgets.QScrollArea(self)
        self.scrollbar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollbar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollbar.setGeometry(QRect(10, 10, 581, 681))
        self.scrollbar.setWidgetResizable(True)
        self.scrollbar.setWidget(self.gridLayoutWidget)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self): #Funzione che connette i pulsanti alle rispettive funzioni
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_plus.setText(QCoreApplication.translate("InserisciProdotto", "+"))
        self.pushButton_plus.clicked.connect(self.add_line)

        self.pushButton_ok.setText(QCoreApplication.translate("InserisciProdotto", "Ok"))
        self.pushButton_ok.clicked.connect(self.add_prodotto)

    def add_info_text(self, nome, label, gridX, gridY): #Funzione che definisce le linee di inserimento del testo e passa il testo alle varie etichette
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        gridLayout2 = QGridLayout()
        gridLayout2.addWidget(etichetta, 0, 0)
        gridLayout2.addWidget(lineEdit, 1, 0)

        self.gridLayout.addLayout(gridLayout2, gridX, gridY)
        self.qlines[nome] = lineEdit

    def add_info_ingredienti(self, label, gridX, gridY, bul): #Funzione che definisce le linee di inserimento per l'ingrediente e passa il testo alle varie etichette
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        gridLayout2 = QGridLayout()
        gridLayout2.addWidget(etichetta, 0, 0)
        gridLayout2.addWidget(lineEdit, 1, 0)
        self.gridLayout.addLayout(gridLayout2, gridX, gridY)

        if bul:
            self.temp = lineEdit
            self.key.append(lineEdit)
        else:
            self.ingredienti[self.temp] = lineEdit

    def add_prodotto(self): #Funzione che controlla il corretto inserimento delle informazioni e conferma la'ggiunta del nuovo prodotto alla lista del Menu
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

        for i in range(len(self.key)):
            self.alimenti[self.key[i].text()] = self.ingredienti[self.key[i]].text()
        self.controller.aggiungi_prodotto(ProdottoSingolo(self.qlines["prodotto"].text(), self.qlines["prezzo"].text(), self.alimenti))
        self.callback()
        self.close()

    def add_line(self): #Funzione che permette di aggiungere una nuova linea di testo per l'ingrediente aggiuntivo
        self.add_info_ingredienti('<font face="Eras Demi ITC"> <font size="10"> Ingredienti: </font>', self.last, 0, True)
        self.add_info_ingredienti('<font face="Eras Demi ITC"> <font size="10"> Quantità: </font>', self.last, 1, False)
        self.last += 1
        self.gridLayout.removeWidget(self.pushButton_plus)
        self.gridLayout.removeWidget(self.pushButton_ok)
        self.gridLayout.addWidget(self.pushButton_plus, self.last, 0)
        self.gridLayout.addWidget(self.pushButton_ok, self.last, 1)

