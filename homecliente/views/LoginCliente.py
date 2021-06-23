from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QMessageBox, QPushButton

from homecliente.views.VistaHomeCliente import VistaHomeCliente


class LoginCliente(QWidget):
    def __init__(self):
        super(LoginCliente, self).__init__()
        self.setWindowTitle('Login Cliente')
        self.resize(500, 120)

        layout = QGridLayout()

        self.label_name = QLabel('<font size="4"> Nome </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Please enter your name')
        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        self.label_number = QLabel('<font size="4"> Numero </font>')
        self.lineEdit_number = QLineEdit()
        self.lineEdit_number.setPlaceholderText('Please enter your table number')
        layout.addWidget(self.label_number, 1, 0)
        layout.addWidget(self.lineEdit_number, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def check(self):
        msg = QMessageBox()

        if self.lineEdit_name.text() == "" or self.lineEdit_number.text() == "" :
            msg.setText('Non hai inserito nome e/o numero!')
            msg.setWindowTitle("Attenzione!")
            msg.exec_()
        else:
            self.run_home_cliente()
            self.close()

    def run_home_cliente(self):
        self.home_cliente= VistaHomeCliente(self.lineEdit_name.text(), self.lineEdit_number.text())
        self.home_cliente.show()
        self.close()