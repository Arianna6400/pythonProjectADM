import os
import pickle

from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni


class ControlloreListaPrenotazioni:

    def __init__(self):
        super(ControlloreListaPrenotazioni, self).__init__()
        self.model = ListaPrenotazioni()
        if os.path.isfile('listaprenotazioni/data/listaprenotazioni.pickle'):
            with open('listaprenotazioni/data/listaprenotazioni.pickle', 'rb') as f:
                self.model = pickle.load(f)

    def aggiungi_prenotazione(self, prenotazione):
        self.model.lista_prenotazioni.append(prenotazione)

    def elimina_prenotazione(self, index):
        self.model.lista_prenotazioni.remove(self.model.lista_prenotazioni[index])

    def get_prenotazioni_by_data(self, data):
        lista = []
        for i in range(len(self.model.lista_prenotazioni)):
            if data.date() == self.model.lista_prenotazioni[i].data.date():
                print(self.model.lista_prenotazioni[i].nome)
                lista.append(self.model.lista_prenotazioni[i])
        return lista

    def get_lista_prenotazione(self):
        return self.model.lista_prenotazioni

    def save_data(self):
        with open('listaprenotazioni/data/listaprenotazioni.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
