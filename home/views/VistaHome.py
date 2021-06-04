from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from homeamministratore.views.LoginAmministratore import LoginAmministratore
from homecliente.views.LoginCliente import LoginCliente
from homecliente.views.VistaHomeCliente import VistaHomeCliente
from homeamministratore.views.VistaHomeAmministratore import VistaHomeAmministratore


class VistaHome(QWidget):
    def __init__(self):

        super(VistaHome, self).__init__()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Amministratore", self.go_login_amministratore), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Cliente", self.go_login_cliente), 0, 1)

        self.setLayout(grid_layout)
        self.resize(600, 300)
        self.setWindowTitle("Donegal Irish Pub")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_vista_cliente(self):
        self.vista_cliente = VistaHomeCliente()
        self.vista_cliente.show()

    def go_vista_amministratore(self):
        self.vista_amministratore = VistaHomeAmministratore()
        self.vista_amministratore.show()

    def go_login_amministratore(self):
        self.login_amministratore = LoginAmministratore()
        self.login_amministratore.show()
        self.go_vista_amministratore

    def go_login_cliente(self):
        self.login_cliente = LoginCliente()
        self.login_cliente.show()
        self.go_login_cliente

