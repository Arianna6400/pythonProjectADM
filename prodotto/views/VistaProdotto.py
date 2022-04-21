from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication, Qt, QSize, QRect
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QScrollBar

from prodotto.controller.ControlloreProdotto import ControlloreProdotto


# Questa vista permette di visualizzare il prodotto singolo

class VistaProdotto(QWidget):

    def __init__(self, prodotto):
        super(VistaProdotto, self).__init__()
        self.controller = ControlloreProdotto(prodotto)

        # Definizione della parte statica, che comprende la dimensione della finestra e il colore in background

        self.setWindowTitle('Vista Prodotto')
        self.resize(600, 700)
        self.setStyleSheet("background-color: rgb(209, 207, 207);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Definizione della griglia con layout verticale nella quale sono presenti sono presenti le informazioni del prodotto

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 681))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setGeometry(QRect(10, 10, 581, 681))
        self.label_name = QLabel(self.verticalLayoutWidget)  # Label in cima nel quale è stampato il nome del prodotto
        self.label_name.setObjectName("label_name")
        self.label_name.setStyleSheet("font: 24pt \"Eras Demi ITC\";")

        self.verticalLayout.addWidget(self.label_name)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout.addItem(self.verticalSpacer)

        # Definizione con codice in formato HTML delle etichette contenenti le informazioni del dipendente

        self.verticalLayout.addWidget(self.get_info(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">Prodotto: {}</span></p></body></html>".format(
                self.controller.get_prodotto())))
        self.verticalLayout.addWidget(self.get_info(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">Prezzo: {}€\n</span></p></body></html>".format(
                self.controller.get_prezzo())))
        self.verticalLayout.addWidget(self.get_info(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">Ingredienti: </span></p></body></html>"))
        for a in self.controller.get_ingredienti():
            self.verticalLayout.addWidget(self.get_info(
                "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">{}</span></p></body></html>".format(
                    a) +
                "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">({})</span></p></body></html>".format(
                    self.controller.get_ingredienti()[a])))
        self.verticalLayout.addWidget(self.get_info(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">\n{} </span></p></body></html>".format(
                self.controller.get_isDisponibile())))

        # Definizione della barra di scorrimento laterale

        self.scrollbar = QtWidgets.QScrollArea(self)
        self.scrollbar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollbar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollbar.setGeometry(QRect(10, 10, 581, 681))
        self.scrollbar.setWidgetResizable(True)
        self.scrollbar.setWidget(self.verticalLayoutWidget)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_name.setText(QCoreApplication.translate("Form", self.controller.get_prodotto()))

    @staticmethod
    def get_info(text):  # Metodo statico che passa le informazioni alle etichette
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label
