import os
import pickle

from listamenu.controller.ControlloreListaMenu import ControlloreListaMenu
from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione
from listaordinazione.model.ListaOrdinazione import ListaOrdinazione
from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino
from magazzino.model.Magazzino import Magazzino
from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class ControlloreOrdinazione:

    def __init__(self, ordinazione, menu):
        self.model = ordinazione
        self.menu = menu

    def get_nome(self):
        return self.model.nome

    def get_tavolo(self):
        return self.model.tavolo

    def get_ordinazione(self):
        return self.model.ordinazione

    def inserisci_ordinazione(self, prodotto):
        magazzino = ControlloreMagazzino()
        if prodotto.get_isDisponibile() == "Disponibile":
            if prodotto.get_prodotto() in self.model.ordinazione:
                self.model.ordinazione[prodotto.get_prodotto()] += 1
            else:
                self.model.ordinazione[prodotto.get_prodotto()] = 1

            for ingrediente, qt in prodotto.get_ingredienti().items():
                magazzino.add_ingrediente(ingrediente, -float(qt))

            self.menu.update()
            magazzino.save_data()

            return True
        return False

    def elimina_ordinazione(self):
        magazzino = ControlloreMagazzino()
        for prodotto, qt in self.model.ordinazione.items():
            for alimento in self.menu.get_lista_menu():
                controllore_alimento = ControlloreProdotto(alimento)
                if controllore_alimento.get_prodotto() == prodotto:
                    for ingrediente, qt2 in controllore_alimento.get_ingredienti().items():
                        magazzino.add_ingrediente(ingrediente, float(qt2 * qt))

        magazzino.save_data()
        self.menu.update()
        self.model.ordinazione = {}

    def conferma_ordinazione(self):
        lista_ordinazione = ListaOrdinazione()
        if os.path.isfile('listaordinazione/data/lista_ordinazione.pickle'):
            with open('listaordinazione/data/lista_ordinazione.pickle', 'rb') as f:
                lista_ordinazione = pickle.load(f)

        lista_ordinazione.aggiungi_ordinazione(self)

        with open('listaordinazione/data/lista_ordinazione.pickle', 'wb') as handle:
            pickle.dump(lista_ordinazione, handle, pickle.HIGHEST_PROTOCOL)

