from PyQt5.QtWidgets import QWidget, QPushButton, QSizePolicy, QGridLayout


class VistaHomeAmministatore(QWidget):

    def __init__(self):

        super(VistaHomeAmministatore, self).__init__()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.get_generic_button("Lista Prenotazioni", self.go_vista_prenotazioni), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Magazzino", self.go_vista_magazzino), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Stipendi", self.go_vista_stipendi), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_vista_dipendenti), 1, 1)

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

    def go_vista_magazzino(self):
        self.vista_magazzino = VistaMagazzino()
        self.vista_magazzino.show()

    def go_vista_stipendi(self):
        self.vista_stipendi = VistaStipendi()
        self.vista_stipendi.show()

    def go_vista_dipendenti(self):
        self.vista_dipendenti = VistaDipendenti()
        self.vista_dipendenti.show()