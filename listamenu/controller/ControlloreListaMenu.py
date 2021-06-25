from listamenu.model.ListaMenu import ListaMenu
from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino
from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class ControlloreListaMenu:
	def __init__(self):
		super(ControlloreListaMenu, self).__init__()
		self.model = ListaMenu()
		self.magazzino = ControlloreMagazzino()

	def get_lista_menu(self):
		return self.model.get_lista_menu()

	def get_prodotto_by_index(self, index):
		return self.model.get_prodotto_by_index(index)

	def elimina_prodotto(self, index):
		return self.model.elimina_prodotto(index)

	def aggiungi_prodotto(self, prodotto_singolo):
		return self.model.aggiungi_prodotto(prodotto_singolo)

	def change_disponibilita(self, prodotto, b):
		for i in range(self.model.get_lista_menu()):
			if self.model.get_lista_menu()[i] == prodotto:
				self.model.get_lista_menu()[i].change_disp(b)

	def save_data(self):
		self.model.save_data()

	def update(self):
		for prodotto in self.model.get_lista_menu():
			if self.check_prodotto_disponibile(ControlloreProdotto(prodotto)):
				self.change_disponibilita(prodotto, True)
			else:
				self.change_disponibilita(prodotto, False)

	def check_prodotto_disponibile(self, prodotto):
		for ingrediente, qt in prodotto.get_ingredienti().items():
			if self.magazzino.get_qt(ingrediente) < float(qt):
				return False
		return True
