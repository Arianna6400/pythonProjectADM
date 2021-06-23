import pickle
import os.path

class ListaOrdinazione:

    def __init__(self):
        super(ListaOrdinazione, self).__init__()
        self.lista_ordinazione = []

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
