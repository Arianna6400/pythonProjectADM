from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from homeamministratore.views.LoginAmministratore import LoginAmministratore
from homecliente.views.LoginCliente import LoginCliente


class VistaHome(QWidget):
    def __init__(self):
        super(VistaHome, self).__init__()

        self.login_cliente = LoginCliente()
        self.login_amministratore = LoginAmministratore()

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Amministratore",
                                                      lambda: self.login_amministratore.show()), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Cliente",
                                                      lambda: self.login_cliente.show()), 0, 1)

        self.setLayout(grid_layout)
        self.resize(600, 300)
        self.setWindowTitle("Donegal Irish Pub")

    # metodo per generare i bottoni per visualizzare le altre schermate
    @staticmethod
    def get_generic_button(titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button
