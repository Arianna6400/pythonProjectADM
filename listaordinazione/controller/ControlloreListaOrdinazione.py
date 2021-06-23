import os
import pickle

from listaordinazione.model.ListaOrdinazione import ListaOrdinazione


class ControlloreListaOrdinazione:
    def __init__(self):
        super(ControlloreListaOrdinazione, self).__init__()
        self.model = ListaOrdinazione()
        if os.path.isfile('listaordinazione/data/lista_ordinazione.pickle'):
            with open('listaordinazione/data/lista_ordinazione.pickle', 'rb') as f:
                self.model = pickle.load(f)

    def get_lista_ordinazione(self):
        return self.model.get_lista_ordinazione()

    def get_ordinazione_by_index(self, index):
        return self.model.get_ordinazione_by_index(index)

    def elimina_ordinazione(self, index):
        return self.model.elimina_ordinazione(index)

    def aggiungi_ordinazione(self, ordinazione):
        return self.model.aggiungi_ordinazione(ordinazione)

    def save_data(self):
        self.model.save_data()
