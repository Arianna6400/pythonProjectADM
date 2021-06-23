from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout

from listamenu.views.VistaListaMenuAmministratore import VistaListaMenuAmministratore
from listaordinazione.views.VistaListaOrdinazione import VistaListaOrdinazione


class VistaHomeAmministratore(QWidget):

    def __init__(self):

        super(VistaHomeAmministratore, self).__init__()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_vista_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Menu", self.go_vista_menu), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Stipendi", self.go_vista_stipendi), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_vista_dipendenti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Ordinazioni", self.go_vista_ordinazione), 2, 0)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Vista Amministratore")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_vista_prenotazioni(self):
        self.vista_prenotazioni = VistaPrenotazioni()
        self.vista_prenotazioni.show()
        self.close()

    def go_vista_menu(self):
        self.vista_menu = VistaListaMenuAmministratore()
        self.vista_menu.show()
        self.close()

    def go_vista_ordinazione(self):
        self.vista_ordinazione = VistaListaOrdinazione()
        self.vista_ordinazione.show()
        self.close()

    def go_vista_stipendi(self):
        self.vista_stipendi = VistaStipendi()
        self.vista_stipendi.show()
        self.close()

    def go_vista_dipendenti(self):
        self.vista_dipendenti = VistaDipendenti()
        self.vista_dipendenti.show()
        self.close()
