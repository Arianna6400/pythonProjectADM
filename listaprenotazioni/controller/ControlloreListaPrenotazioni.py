import os
import pickle

from datetime import datetime
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
        self.save_data()

    def elimina_prenotazione(self, prenotazione):
        for i in range(len(self.model.lista_prenotazioni)):
            if i == len(self.model.lista_prenotazioni) + 1:
                break

            if prenotazione.telefono == self.model.lista_prenotazioni[i].telefono:
                del self.model.lista_prenotazioni[i]

        self.save_data()

    def get_prenotazioni_by_data(self, data):
        lista = []
        for i in range(len(self.model.lista_prenotazioni)):
            if data.date() == self.model.lista_prenotazioni[i].data.date():
                lista.append(self.model.lista_prenotazioni[i])
        return lista

    def get_lista_prenotazione(self):
        return self.model.lista_prenotazioni

    def save_data(self):
        date = datetime.now()

        for prenotazione in self.model.lista_prenotazioni:  # cancella in modo automatico le prenotazioni passate
            if date > prenotazione.data:
                self.model.lista_prenotazioni.remove(prenotazione)

        with open('listaprenotazioni/data/listaprenotazioni.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

