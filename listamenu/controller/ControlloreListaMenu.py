from listamenu.model.ListaMenu import ListaMenu


class ControlloreListaMenu:
	def __init__(self):
		super(ControlloreListaMenu, self).__init__()
		self.model = ListaMenu()

	def get_lista_menu(self):
		return self.model.get_lista_menu()

	def get_prodotto_by_index(self, index):
		return self.model.get_prodotto_by_index(index)

	def elimina_prodotto(self, index):
		return self.model.elimina_prodotto(index)

	def aggiungi_prodotto(self, prodotto_singolo):
		return self.model.aggiungi_prodotto(prodotto_singolo)

	def save_data(self):
		self.model.save_data()
