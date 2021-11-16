from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listamenu.controller.ControlloreListaMenu import ControlloreListaMenu
from prodotto.views.VistaInserisciProdotto import VistaInserisciProdotto
from prodotto.views.VistaProdotto import VistaProdotto


class VistaListaMenuAmministratore(QWidget):
	def __init__(self):
		super(VistaListaMenuAmministratore, self).__init__()

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

		add_button = QPushButton("Inserisci")
		add_button.clicked.connect(self.add_info)
		buttons_layout.addWidget(add_button)

		delete_button = QPushButton("Elimina")
		delete_button.clicked.connect(self.delete_selected_info)
		buttons_layout.addWidget(delete_button)

		buttons_layout.addStretch()
		self.h_layout.addLayout(buttons_layout)

		self.setLayout(self.h_layout)
		self.resize(600, 300)
		self.setWindowTitle("Lista Menu")

	def closeEvent(self, event):
		self.controller.save_data()
		event.accept()

	def show_selected_info(self):  # metodo per visualizzare le informazioni del prodotto selezionato
		if len(self.list_view.selectedIndexes()) > 0:
			selected = self.list_view.selectedIndexes()[0].row()
			prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
			self.vista_prodotto = VistaProdotto(prodotto_selezionato)
			self.vista_prodotto.show()

	def delete_selected_info(self):  # metodo per rimuove un prodotto dal menu
		if len(self.list_view.selectedIndexes()) > 0:
			selected = self.list_view.selectedIndexes()[0].row()
			prodotto_selezionato = self.controller.get_prodotto_by_index(selected)
			self.controller.elimina_prodotto(prodotto_selezionato)
			self.update_ui()
			self.h_layout.replaceWidget(self.list_view, self.list_view)

	def add_info(self):  # metodo per inserire un nuovo prodotto nel menu
		self.vista_inserisci_prodotto = VistaInserisciProdotto(self.controller, self.update_ui)
		self.vista_inserisci_prodotto.show()

	def update_ui(self):  # metodo per aggiornare la lista del menu in caso venga effettuata una modifica
		self.listview_model = QStandardItemModel(self.list_view)
		for prodotto in self.controller.get_lista_menu():
			item = QStandardItem()
			item.setText(prodotto.prodotto + " {}".format(prodotto.prezzo) + "€")
			item.setEditable(False)
			font = item.font()
			font.setPointSize(18)
			item.setFont(font)
			self.listview_model.appendRow(item)
		self.list_view.setModel(self.listview_model)
