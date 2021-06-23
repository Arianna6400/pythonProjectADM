import os
import pickle

from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione


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
        self.lista_ordinazione = ControlloreListaOrdinazione()
        if os.path.isfile('listaordinazione/data/lista_ordinazione.pickle'):
            with open('listaordinazione/data/lista_ordinazione.pickle', 'rb') as f:
                self.lista_ordinazione = pickle.load(f)

        self.lista_ordinazione.aggiungi_ordinazione(self)

        with open('listaordinazione/data/lista_ordinazione.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordinazione, handle, pickle.HIGHEST_PROTOCOL)