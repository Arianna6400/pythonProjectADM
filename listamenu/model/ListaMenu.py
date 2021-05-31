import json
import pickle
import os.path

from prodotto.model.ProdottoSingolo import ProdottoSingolo


class ListaMenu:

	def __init__(self):
		super(ListaMenu, self).__init__()
		self.lista_menu = []
		if os.path.isfile('listamenu/data/lista_menu.pickle'):
			with open('listamenu/data/lista_menu.pickle', 'rb') as f:
				self.lista_menu = pickle.load(f)
		else:
			with open('listamenu/data/lista_menu_iniziale.json') as f:
				lista_menu_iniziale = json.load(f)
			for menu_iniziale in lista_menu_iniziale:
				self.aggiungi_prodotto(ProdottoSingolo(menu_iniziale["prodotto"], menu_iniziale["prezzo"], menu_iniziale["ingredienti"]))

	def aggiungi_prodotto(self, prodotto_singolo):
		self.lista_menu.append(prodotto_singolo)

	def elimina_menu(self, index):
		self.lista_menu.remove(index)

	def get_Menu_by_index(self, index):
		return self.lista_menu[index]

	def get_lista_menu(self):
		return self.lista_menu

	def save_data(self):
		with open('listamenu/data/lista_menu.pickle', 'wb') as handle:
			pickle.dump(self.lista_menu, handle, pickle.HIGHEST_PROTOCOL)
