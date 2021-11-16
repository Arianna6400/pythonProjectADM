from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from homeamministratore.views.VistaHomeAmministratore import VistaHomeAmministratore


class LoginAmministratore(QWidget):
    def __init__(self):
        super(LoginAmministratore, self).__init__()
        self.setWindowTitle('Login Amministratore')
        self.resize(500, 300)
        self.setStyleSheet("background-color: white;\n")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        layout = QGridLayout()

        label_name = QLabel('<font size="5"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        self.lineEdit_username.returnPressed.connect(self.check_password)
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="5"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        self.lineEdit_password.returnPressed.connect(self.check_password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        self.button_login = QPushButton('Login')
        self.button_login.setStyleSheet("background-color: rgb(197, 255, 134);\n")
        self.button_login.setGeometry(QRect(150, 230, 201, 28))
        self.button_login.clicked.connect(self.check_password)
        layout.addWidget(self.button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check_password(self):

        if self.lineEdit_username.text() == 'Admin' and self.lineEdit_password.text() == '666':  # da rimettere l'username corretto
            self.run_home_amministratore()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Attenzione!")
            msg.setText(
                "Hai inserito un username o password errati!")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('listamenu/data/images/logo_donegal.png'), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

    def run_home_amministratore(self):
        self.home_amministratore = VistaHomeAmministratore()
        self.home_amministratore.showMaximized()
