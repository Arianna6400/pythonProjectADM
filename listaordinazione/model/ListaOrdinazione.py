import json
import pickle
import os.path

from ordinazione.model.Ordinazione import Ordinazione


class ListaOrdinazione:

    def __init__(self):
        super(ListaOrdinazione, self).__init__()
        self.lista_ordinazione = []
        if os.path.isfile('listaordinazione/data/lista_ordinazione.pickle'):
            with open('listaordinazione/data/lista_ordinazione.pickle', 'rb') as f:
                self.lista_ordinazione = pickle.load(f)
        else:
            with open('listaordinazione/data/lista_ordinazione_iniziale.json') as f:
                lista_ordinazione_iniziale = json.load(f)
            for ordinazione_iniziale in lista_ordinazione_iniziale:
                self.aggiungi_ordinazione(Ordinazione(ordinazione_iniziale["tavolo"], ordinazione_iniziale["nome"]))

    def aggiungi_ordinazione(self, ordinazione):
        self.lista_ordinazione.append(ordinazione)

    def elimina_ordinazione(self, index):
        self.lista_ordinazione.remove(index)

    def get_ordinazione_by_index(self, index):
        return self.lista_ordinazione[index]

    def get_lista_ordinazione(self):
        return self.lista_ordinazione

    def save_data(self):
        with open('listaordinazione/data/lista_ordinazione.pickle', 'wb') as handle:
            pickle.dump(self.lista_ordinazione, handle, pickle.HIGHEST_PROTOCOL)
