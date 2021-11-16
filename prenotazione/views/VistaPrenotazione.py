from datetime import datetime, timedelta
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prenotazione.model.Prenotazione import Prenotazione


class VistaPrenotazione(QWidget):
    def __init__(self, controller):

        super(VistaPrenotazione, self).__init__()

        self.controller = controller
        self.qlines = []

        self.setWindowTitle('Nuova Prenotazione')
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
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Nome: </font>', 0, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Telefono: </font>', 1, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Numero persone: </font>', 2, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Data (dd/MM/yyyy): </font>', 3, 0)
        self.add_info_text('<font face="Eras Demi ITC"> <font size="8"> Orario: </font>', 4, 0)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(self.verticalSpacer)

        self.pushButton_ok = QPushButton(self.gridLayoutWidget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_ok.setStyleSheet("border-radius:22px;\n"
                                         "background-color: rgb(197, 255, 134);\n"
                                         "color:black;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: black;\n"
                                         "font: 12pt \"Eras Demi ITC\";")

        self.gridLayout.addWidget(self.pushButton_ok, 5, 0)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.pushButton_ok.setText(QCoreApplication.translate("InserisciProdotto", "Ok"))
        self.pushButton_ok.clicked.connect(self.add_prenotazione)

    def add_info_text(self, label, gridX, gridY):
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        gridLayout2 = QGridLayout()
        gridLayout2.addWidget(etichetta, 0, 0)
        gridLayout2.addWidget(lineEdit, 1, 0)

        self.gridLayout.addLayout(gridLayout2, gridX, gridY)
        self.qlines.append(lineEdit)

    @staticmethod
    def validate(date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def add_prenotazione(self):
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
        new_data = data + timedelta(hours=int(self.qlines[4].text()))
        self.controller.aggiungi_prenotazione(Prenotazione(self.qlines[0].text(), self.qlines[1].text(), self.qlines[2].text(), new_data))
        self.close()

