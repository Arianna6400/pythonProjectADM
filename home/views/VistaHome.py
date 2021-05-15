from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from homecliente.views.VistaHomeCliente import VistaHomeCliente
from homeamministratore.views.VistaHomeAmministratore import VistaHomeAmministratore


class VistaHome(QWidget):
    def __init__(self):

        super(VistaHome, self).__init__()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Amministratore", self.go_vista_amministratore), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Cliente", self.go_vista_cliente), 0, 1)

        self.setLayout(grid_layout)
        self.resize(400, 300)
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
