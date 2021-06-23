import os
import pickle

from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione
from listaordinazione.model.ListaOrdinazione import ListaOrdinazione


class ControlloreOrdinazione:

    def __init__(self, ordinazione):
        self.model = ordinazione

    def get_nome(self):
        return self.model.nome

    def get_tavolo(self):
        return self.model.tavolo

    def get_ordinazione(self):
        return self.model.ordinazione

    def inserisci_ordinazione(self, prodotto):
        if prodotto.prodotto in self.model.ordinazione:
            self.model.ordinazione[prodotto.prodotto] += 1
        else:
            self.model.ordinazione[prodotto.prodotto] = 1

    def elimina_ordinazione(self, prodotto):
        if prodotto.prodotto in self.model.ordinazione:
            del self.model.ordinazione[prodotto.prodotto]

    def elimina_ordinazione(self):
        self.model.ordinazione = {}

    def conferma_ordinazione(self):
        lista_ordinazione = ListaOrdinazione()
        if os.path.isfile('listaordinazione/data/lista_ordinazione.pickle'):
            with open('listaordinazione/data/lista_ordinazione.pickle', 'rb') as f:
                lista_ordinazione = pickle.load(f)

        lista_ordinazione.aggiungi_ordinazione(self)

        with open('listaordinazione/data/lista_ordinazione.pickle', 'wb') as handle:
            pickle.dump(lista_ordinazione, handle, pickle.HIGHEST_PROTOCOL)
