from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listamenu.controller.ControlloreListaMenu import ControlloreListaMenu
from menu.views.VistaMenuCliente import VistaMenu


class VistaListaMenuAmministratore(QWidget):
	def __init__(self):
		super(VistaListaMenuAmministratore, self).__init__()

		self.controller = ControlloreListaMenu()

		h_layout = QHBoxLayout()
		self.list_view = QListView()
		self.listview_model = QStandardItemModel(self.list_view)
		for Menu in self.controller.get_lista_menu():
			item = QStandardItem()
			item.setText("{} ".format(Menu.prodotto) + "{}€".format(Menu.prezzo))
			item.setEditable(False)
			font = item.font()
			font.setPointSize(18)
			item.setFont(font)
			self.listview_model.appendRow(item)
		self.list_view.setModel(self.listview_model)
		h_layout.addWidget(self.list_view)

		buttons_layout = QVBoxLayout()

		open_button = QPushButton("Apri")
		# open_button.clicked.connect(self.show_selected_info())
		buttons_layout.addWidget(open_button)

		add_button = QPushButton("Inserisci")
		# add_button.clicked.connect(self.add_info())
		buttons_layout.addWidget(add_button)

		delete_button = QPushButton("Elimina")
		# delete_button.clicked.connect(self.delete_selected_info())
		buttons_layout.addWidget(delete_button)

		buttons_layout.addStretch()
		h_layout.addLayout(buttons_layout)

		self.setLayout(h_layout)
		self.resize(600, 300)
		self.setWindowTitle("Lista Menu")

	def closeEvent(self, event):
		print("ON CLOSE")
		self.controller.save_data()
		event.accept()

	def show_selected_info(self):
		selected = self.list_view.selectedIndexes()[0].row()
		Menu_selezionato = self.controller.get_menu_by_index(selected)
		self.vista_Menu = VistaMenu(Menu_selezionato)
		# self.

