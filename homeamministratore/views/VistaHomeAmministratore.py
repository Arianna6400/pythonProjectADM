from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout

from listadipendenti.views.VistaListaDipendente import VistaListaDipendenti
from listamenu.views.VistaListaMenuAmministratore import VistaListaMenuAmministratore
from listaordinazione.views.VistaListaOrdinazione import VistaListaOrdinazione
from listaprenotazioni.views.VistaListaPrenotazioni import VistaListaPrenotazioni
from magazzino.views.VistaMagazzino import VistaMagazzino


class VistaHomeAmministratore(QWidget):

    def __init__(self):  # all'inzio viene generata una griglia con le possibili scelte dell'amministratore

        super(VistaHomeAmministratore, self).__init__()

        self.vista_dipendenti = VistaListaDipendenti()
        self.vista_magazzino = VistaMagazzino()
        self.vista_ordinazione = VistaListaOrdinazione()
        self.vista_menu = VistaListaMenuAmministratore()
        self.vista_prenotazioni = VistaListaPrenotazioni()

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", lambda: self.vista_prenotazioni.show()), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Menu", lambda: self.vista_menu.show()), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Magazzino", lambda: self.vista_magazzino.show()), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", lambda: self.vista_dipendenti.show()), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Lista Ordinazioni", lambda: self.vista_ordinazione.show()), 2, 0)
        grid_layout.addWidget(self.get_generic_button("Quit", lambda: self.close()), 2, 1)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Vista Amministratore")

    @staticmethod
    def get_generic_button(titolo, on_click):  # metodo per generare i bottoni che visualizzeranno le rispettive viste
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button
