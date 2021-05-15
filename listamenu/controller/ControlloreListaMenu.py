from listamenu.model.ListaMenu import ListaMenu


class ControlloreListaMenu:
	def __init__(self):
		super(ControlloreListaMenu, self).__init__()
		self.model = ListaMenu()

	def get_lista_menu(self):
		return self.model.get_lista_menu()

	def get_menu_by_index(self, index):
		return self.model.get_menu_by_index(index)

	def save_data(self):
		self.model.save_data()
