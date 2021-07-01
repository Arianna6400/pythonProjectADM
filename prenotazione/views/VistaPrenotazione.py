from datetime import datetime, timedelta

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QGridLayout

from prenotazione.model.Prenotazione import Prenotazione
from prodotto.model.ProdottoSingolo import ProdottoSingolo


class VistaPrenotazione(QWidget):
    def __init__(self, controller):
        super(VistaPrenotazione, self).__init__()
        self.controller = controller

        self.layout = QGridLayout()
        self.qlines = []

        self.add_info_text("Nome:", 0, 0)
        self.add_info_text("Telefono:", 1, 0)
        self.add_info_text("Numero persone:", 2, 0)
        self.add_info_text("Data (dd/MM/yyyy):", 3, 0)
        self.add_info_text("Orario:", 4, 0)

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.add_prenotazione)
        self.layout.addWidget(self.btn_ok, 5, 0)

        self.setLayout(self.layout)
        self.setWindowTitle("Aggiungi Prenotazione")

    def add_info_text(self, label, gridX, gridY):
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        layout2 = QGridLayout()
        layout2.addWidget(etichetta, 0, 0)
        layout2.addWidget(lineEdit, 1, 0)

        self.layout.addLayout(layout2, gridX, gridY)
        self.qlines.append(lineEdit)

    @staticmethod
    def validate(date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def add_prenotazione(self):
        for value in self.qlines:
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        if not self.validate(self.qlines[3].text()):
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci la data nel formato richiesto!', QMessageBox.Ok, QMessageBox.Ok)
            return
        data = datetime.strptime(self.qlines[3].text(), '%d/%m/%Y')
        new_data = data + timedelta(hours=int(self.qlines[4].text()))
        self.controller.aggiungi_prenotazione(Prenotazione(self.qlines[0].text(), self.qlines[1].text(), self.qlines[2].text(), new_data))
        self.close()

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
