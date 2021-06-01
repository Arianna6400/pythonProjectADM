from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, QMessageBox, QGridLayout

from prodotto.model.ProdottoSingolo import ProdottoSingolo


class VistaInserisciProdotto(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciProdotto, self).__init__()
        self.controller = controller
        self.callback = callback
        self.last = 3
        self.ingredienti = {}
        self.temp = ""
        self.key = []
        self.alimenti = {}

        self.layout = QGridLayout()
        self.qlines = {}

        self.add_info_text("prodotto", "Prodotto:", 0, 0)
        self.add_info_text("prezzo", "Prezzo:", 1, 0)
        self.add_info_ingredienti("Ingredienti:", 2, 0, True)
        self.add_info_ingredienti("Quantità:", 2, 1, False)

        self.layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.btn_add = QPushButton("+")
        self.btn_add.clicked.connect(self.add_line)
        self.layout.addWidget(self.btn_add, self.last, 0)

        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.add_prodotto)
        self.layout.addWidget(self.btn_ok, self.last, 1)

        self.setLayout(self.layout)
        self.setWindowTitle("Aggiungi Prodotto")

    def add_info_text(self, nome, label, gridX, gridY):
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        layout2 = QGridLayout()
        layout2.addWidget(etichetta, 0, 0)
        layout2.addWidget(lineEdit, 1, 0)

        self.layout.addLayout(layout2, gridX, gridY)
        self.qlines[nome] = lineEdit

    def add_info_ingredienti(self, label, gridX, gridY, bul):
        etichetta = QLabel(label)
        lineEdit = QLineEdit()
        layout2 = QGridLayout()
        layout2.addWidget(etichetta, 0, 0)
        layout2.addWidget(lineEdit, 1, 0)
        self.layout.addLayout(layout2, gridX, gridY)

        if bul:
            self.temp = lineEdit
            self.key.append(lineEdit)
        else:
            self.ingredienti[self.temp] = lineEdit

    def add_prodotto(self):
        for value in self.qlines.values():
            if value.text() == "":
                QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste.', QMessageBox.Ok, QMessageBox.Ok)
                return

        for i in range(len(self.key)):
            self.alimenti[self.key[i].text()] = self.ingredienti[self.key[i]].text()
        self.controller.aggiungi_prodotto(ProdottoSingolo(self.qlines["prodotto"].text(), self.qlines["prezzo"].text(), self.alimenti))
        print(self.ingredienti)
        self.callback()
        self.close()

    def add_line(self):
        self.add_info_ingredienti("Ingredienti:", self.last, 0, True)
        self.add_info_ingredienti("Quantità:", self.last, 1, False)
        self.last += 1
        self.layout.removeWidget(self.btn_add)
        self.layout.removeWidget(self.btn_ok)
        self.layout.addWidget(self.btn_add, self.last, 0)
        self.layout.addWidget(self.btn_ok, self.last, 1)
