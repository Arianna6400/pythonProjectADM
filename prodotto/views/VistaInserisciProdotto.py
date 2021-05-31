from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox

from prodotto.model.ProdottoSingolo import ProdottoSingolo


class VistaInserisciProdotto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        self.callback = callback

        self.v_layout = QVBoxLayout()
        self.qlines = {}
        self.add_info_text("prodotto", "Prodotto")
        self.add_info_text("prezzo", "Prezzo")
        self.add_info_text("ingredienti", "Ingredienti")

        self.v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_prodotto)
        self.v_layout.addWidget(btn_ok)

        self.setLayout(self.v_layout)
        self.setWindowTitle("Aggiungi Prodotto")

    def add_info_text(self, nome, label):
        self.v_layout.addWidget(QLabel(label))
        current_text = QLineEdit(self)
        self.qlines[nome] = current_text
        self.v_layout.addWidget(current_text)

    def add_prodotto(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return
        self.controller.aggiungi_prodotto(ProdottoSingolo(self.qlines["prodotto"].text(), self.qlines["prezzo"], self.qlines["ingredienti"].text()))
        # Sistemare il discorso dell'aggiunta di ingredienti non come stringa
        self.callback()
        self.close()