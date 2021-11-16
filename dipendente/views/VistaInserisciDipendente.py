from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from dipendente.controller.ControlloreDipendente import ControlloreDipendente
from dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.info_dipendente = {}  # dizionario in cui andranno tutte le informazioni riguardanti un dipendente
        self.add_info_text("id", "ID")
        self.add_info_text("nome", "Nome")
        self.add_info_text("cognome", "Cognome")
        self.add_info_text("cf", "Codice Fiscale")
        self.add_info_text("data_n", "Data di nascita (dd/MM/yyyy)")
        self.add_info_text("luogo_n", "Luogo di nascita")
        self.add_info_text("telefono", "Telefono")
        self.add_info_text("ruolo", "Ruolo")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")  # bottone per confermare i dati inseriti
        btn_ok.clicked.connect(self.add_dipendente)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Nuovo Dipendente")

    # metodo che genera le caselle di testo dove inserire le informazioni del dipendente
    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        current_text.returnPressed.connect(self.add_dipendente)
        self.info_dipendente[nome] = current_text
        self.v_layout.addWidget(current_text)

    # metodo collegato alla conferma dei dati del dipendente
    def add_dipendente(self):
        for value in self.info_dipendente.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

        try:
            datetime.strptime(self.info_dipendente["data_n"].text(), '%d/%m/%Y')
        except ValueError:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci una data valida nel formato dd/MM/yyyy.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        if not len(self.info_dipendente["cf"].text()) == 16:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un codice fiscale valido.',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        for dipendente in self.controller.get_lista_dipendenti():
            if dipendente.cf == self.info_dipendente["cf"].text():
                QMessageBox.critical(self, 'Errore', 'Il dipendente che si vuole inserire è gia presente nella '
                                                     'lista dei dipendenti.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

        if not len(self.info_dipendente["telefono"].text()) == 10:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un numero di telefono valido!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        # aggiunta del nuovo dipendente nella lista dei dipendente dopo un controllo dei dati inseriti
        self.controller.aggiungi_dipendente(ControlloreDipendente(
            self.info_dipendente["id"].text(),
            self.info_dipendente["nome"].text(),
            self.info_dipendente["cognome"].text(),
            self.info_dipendente["data_n"].text(),
            self.info_dipendente["luogo_n"].text(),
            self.info_dipendente["cf"].text(),
            self.info_dipendente["telefono"].text(),
            self.info_dipendente["ruolo"].text())
        )
        self.callback()
        self.close()
