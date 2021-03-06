from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton

from homecliente.views.VistaHomeCliente import VistaHomeCliente


# Classe che definisce la schermata di Login per l'interfaccia del Cliente

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

        # Label che contiene la linea di scrittura del nome

        self.label_name = QLabel('<font size="5"> Nome </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Please enter your name')
        self.lineEdit_name.returnPressed.connect(self.check)
        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        # Label che contiene la linea di scrittura del numero del tavolo

        self.label_number = QLabel('<font size="5"> Numero </font>')
        self.lineEdit_number = QLineEdit()
        self.lineEdit_number.setPlaceholderText('Please enter your table number')
        self.lineEdit_number.returnPressed.connect(self.check)
        layout.addWidget(self.label_number, 1, 0)
        layout.addWidget(self.lineEdit_number, 1, 1)

        # Pulsante che, una volta controllata la funzione di check, permette di accedere alla vista successiva

        self.button_login = QPushButton('Login')
        self.button_login.setStyleSheet("background-color: rgb(209, 207, 207);\n")
        self.button_login.setGeometry(QRect(150, 230, 201, 28))
        self.button_login.clicked.connect(self.check)
        layout.addWidget(self.button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check(self):  # Funzione di controllo dell'inserimento delle credenziali corrette
        if (self.lineEdit_name.text() == "" or self.lineEdit_name.text().isdigit()) or (
                self.lineEdit_number.text() == "" or self.lineEdit_number.text().isalpha()) or (
                int(self.lineEdit_number.text()) > 30) or (int(self.lineEdit_number.text()) < 1):
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

    def run_home_cliente(self):  # Funzione che permette di accedere alla Vista Cliente una volta effettuato correttamente il Login
        self.home_cliente = VistaHomeCliente(self.lineEdit_name.text(), self.lineEdit_number.text())
        self.home_cliente.showMaximized()
        self.close()
