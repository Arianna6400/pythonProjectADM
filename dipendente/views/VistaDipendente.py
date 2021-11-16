from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, controllore, callback):
        super(VistaDipendente, self).__init__()
        self.controller = ControlloreDipendente(dipendente)
        self.controllore = controllore
        self.callback = callback

        self.setWindowTitle('Vista Dipendente')
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb(235, 255, 219);")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.verticalLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.label_name.setStyleSheet("font: 24pt \"Eras Demi ITC\";")

        self.verticalLayout.addWidget(self.label_name)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Codice Fiscale: {}</span></p></body></html>".format(self.controller.get_cf_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Data Nascita: {}</span></p></body></html>".format(self.controller.get_data_nascita_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Luogo Nascita: {}</span></p></body></html>".format(self.controller.get_luogo_nascita_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Telefono: {}</span></p></body></html>".format(self.controller.get_telefono_dipendente())))
        self.verticalLayout.addWidget(self.get_info("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Ruolo: {}</span></p></body></html>".format(self.controller.get_ruolo_dipendente())))

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton_delete = QPushButton(self.verticalLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setStyleSheet("border-radius:22px;\n"
                                             "background-color: rgb(197, 255, 134);\n"
                                             "color:black;\n"
                                             "border-style: outset;\n"
                                             "border-width: 2px;\n"
                                             "border-color: black;\n"
                                             "font: 12pt \"Eras Demi ITC\";")

        self.verticalLayout.addWidget(self.pushButton_delete)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_name.setText(QCoreApplication.translate("Form", self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente()))
        self.pushButton_delete.setText(QCoreApplication.translate("Form", "Elimina"))
        self.pushButton_delete.clicked.connect(self.elimina_dipendente)

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente(self):
        self.controllore.elimina_dipendente_by_id(self.controller.get_id_dipendente())
        self.callback()
        self.close()
