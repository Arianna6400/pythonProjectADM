from datetime import datetime, timedelta

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QGridLayout

from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from prenotazione.model.Prenotazione import Prenotazione


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

    def add_info_text(self, label, gridx, gridy):
        etichetta = QLabel(label)
        line = QLineEdit()
        line.returnPressed.connect(self.add_prenotazione)
        layout2 = QGridLayout()
        layout2.addWidget(etichetta, 0, 0)
        layout2.addWidget(line, 1, 0)

        self.layout.addLayout(layout2, gridx, gridy)
        self.qlines.append(line)

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
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.',
                                     QMessageBox.Ok, QMessageBox.Ok)
                return

        if not self.validate(self.qlines[3].text()):
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci la data nel formato richiesto!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        if not len(self.qlines[1].text()) == 10:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci un numero di telefono valido!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        if not self.qlines[2].text().isdigit():
            QMessageBox.critical(self, 'Errore', 'Per favore inserire un numero di persone valido!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        if int(self.qlines[4].text()) < 18 or int(self.qlines[4].text()) > 24:
            QMessageBox.critical(self, 'Errore', 'Per favore inserire un orario nella quale il locale è aperto!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        data = datetime.strptime(self.qlines[3].text(), '%d/%m/%Y')
        new_data = data + timedelta(hours=int(self.qlines[4].text()))

        if new_data < datetime.now():
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci una data futura!',
                                 QMessageBox.Ok, QMessageBox.Ok)
            return

        self.controller.aggiungi_prenotazione(ControllorePrenotazione(self.qlines[0].text(), self.qlines[1].text(),
                                                                      self.qlines[2].text(), new_data))
        self.close()

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()
