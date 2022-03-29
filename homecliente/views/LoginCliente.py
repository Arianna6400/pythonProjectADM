from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton

from homecliente.views.VistaHomeCliente import VistaHomeCliente


class LoginCliente(QWidget):
    def __init__(self):
        super(LoginCliente, self).__init__()
        self.setWindowTitle('Login Cliente')
        self.resize(500, 300)
        self.setStyleSheet("background-color: white;\n")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        layout = QGridLayout()

        self.label_name = QLabel('<font size="5"> Nome </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Please enter your name')
        self.lineEdit_name.returnPressed.connect(self.check)
        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        self.label_number = QLabel('<font size="5"> Numero </font>')
        self.lineEdit_number = QLineEdit()
        self.lineEdit_number.setPlaceholderText('Please enter your table number')
        self.lineEdit_number.returnPressed.connect(self.check)
        layout.addWidget(self.label_number, 1, 0)
        layout.addWidget(self.lineEdit_number, 1, 1)

        self.button_login = QPushButton('Login')
        self.button_login.setStyleSheet(" background-color: rgb(197, 255, 134);\n")
        self.button_login.setGeometry(QRect(150, 230, 201, 28))
        self.button_login.clicked.connect(self.check)
        layout.addWidget(self.button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check(self):
        if (self.lineEdit_name.text() == "" or self.lineEdit_name.text().isdigit()) or (self.lineEdit_number.text() == "" or self.lineEdit_number.text().isalpha()) or (self.lineEdit_number.text() > "30"):
            msg = QMessageBox()
            msg.setWindowTitle("Attenzione!")
            msg.setText("Potresti non avere inserito nome e/o numero correttamente!\n""Numero massimo di tavoli: 30")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()
        else:
            self.run_home_cliente()
            self.close()

    def run_home_cliente(self):
        self.home_cliente = VistaHomeCliente(self.lineEdit_name.text(), self.lineEdit_number.text())
        self.home_cliente.showMaximized()
        self.close()