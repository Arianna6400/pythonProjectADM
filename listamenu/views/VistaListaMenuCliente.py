from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QMessageBox

from listamenu.controller.ControlloreListaMenu import ControlloreListaMenu
from ordinazione.controller.ControlloreOrdinazione import ControlloreOrdinazione
from ordinazione.model.Ordinazione import Ordinazione
from ordinazione.views.VistaOrdinazione import VistaOrdinazione
from prodotto.views.VistaProdotto import VistaProdotto


class VistaListaMenuCliente(QWidget):

    def __init__(self, nome, tavolo):

        super(VistaListaMenuCliente, self).__init__()

        self.ordinazione = ControlloreOrdinazione(Ordinazione(nome.text(), tavolo.text()))
        self.controller = ControlloreListaMenu()

        self.h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.listview_model = QStandardItemModel(self.list_view)
        for ProdottoSingolo in self.controller.get_lista_menu():
            item = QStandardItem()
            item.setText("{} ".format(ProdottoSingolo.prodotto) + "{}€".format(ProdottoSingolo.prezzo))
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)
        self.h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()

        open_button = QPushButton("Apri")
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        order_button = QPushButton("Aggiungi ordine")
        order_button.clicked.connect(self.add_ordinazione)
        buttons_layout.addWidget(order_button)

        view_button = QPushButton("Visualizza ordine")
        view_button.clicked.connect(self.view_ordinazione)
        buttons_layout.addWidget(view_button)

        check_button = QPushButton("Conferma ordine")
        # check_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(check_button)

        buttons_layout.addStretch()
        self.h_layout.addLayout(buttons_layout)

        self.setLayout(self.h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Menu")

    def closeEvent(self, event):
        print("ON CLOSE")
        self.controller.save_data()
        event.accept()

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
            self.vista_prodotto = VistaProdotto(prodotto_selezionato)
            self.vista_prodotto.show()

    def view_ordinazione(self):

        msg = QMessageBox()

        if self.ordinazione.get_ordinazione():
            self.vista_ordinazione = VistaOrdinazione(self.ordinazione)
            self.vista_ordinazione.show()
        else:
            msg.setText('Ordine vuoto')
            msg.setWindowTitle("Attenzione!")
            msg.exec_()

    def add_ordinazione(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
            self.ordinazione.inserisci_ordinazione(prodotto_selezionato)
