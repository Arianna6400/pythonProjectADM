from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QSpacerItem, QSizePolicy, QPushButton, QLineEdit, QMessageBox, \
    QGridLayout

from prodotto.model.ProdottoSingolo import ProdottoSingolo


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

        self.setWindowTitle('Aggiungi Nuovo Prodotto')
        self.resize(600, 700)
        self.setStyleSheet("background-color: rgb(235, 255, 219);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

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

        self.pushButton_plus = QPushButton(self.gridLayoutWidget)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_plus.setStyleSheet("border-radius:22px;\n"
                                         "background-color: rgb(197, 255, 134);\n"
                                         "color:black;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: black;\n"
                                         "font: 12pt \"Eras Demi ITC\";")

        self.gridLayout.addWidget(self.pushButton_plus, self.last, 0)

        self.pushButton_ok = QPushButton(self.gridLayoutWidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_ok.setStyleSheet("border-radius:22px;\n"
                                         "background-color: rgb(197, 255, 134);\n"
                                         "color:black;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: black;\n"
                                         "font: 12pt \"Eras Demi ITC\";")

        self.gridLayout.addWidget(self.pushButton_ok, self.last, 1)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_plus.setText(QCoreApplication.translate("InserisciProdotto", "+"))
        self.pushButton_plus.clicked.connect(self.add_line)

        self.pushButton_ok.setText(QCoreApplication.translate("InserisciProdotto", "Ok"))
        self.pushButton_ok.clicked.connect(self.add_prodotto)

    def add_info_text(self, nome, label, gridX, gridY):
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        gridLayout2 = QGridLayout()
        gridLayout2.addWidget(etichetta, 0, 0)
        gridLayout2.addWidget(lineEdit, 1, 0)

        self.gridLayout.addLayout(gridLayout2, gridX, gridY)
        self.qlines[nome] = lineEdit

    def add_info_ingredienti(self, label, gridX, gridY, bul):
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

    def add_prodotto(self):
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

    def add_line(self):
        self.add_info_ingredienti('<font face="Eras Demi ITC"> <font size="10"> Ingredienti: </font>', self.last, 0, True)
        self.add_info_ingredienti('<font face="Eras Demi ITC"> <font size="10"> Quantità: </font>', self.last, 1, False)
        self.last += 1
        self.gridLayout.removeWidget(self.pushButton_plus)
        self.gridLayout.removeWidget(self.pushButton_ok)
        self.gridLayout.addWidget(self.pushButton_plus, self.last, 0)
        self.gridLayout.addWidget(self.pushButton_ok, self.last, 1)

