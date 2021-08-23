import json
import os
import pickle

from dipendente.model.Dipendente import Dipendente


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile('listadipendenti/data/lista_dipendenti.pickle'):
            with open('listadipendenti/data/lista_dipendenti.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)
        else:
            with open('listadipendenti/data/lista_dipendenti_iniziale.json') as f:
                lista_dipendenti_iniziale = json.load(f)
            for dipendente in lista_dipendenti_iniziale:
                self.aggiungi_dipendente(
                    Dipendente(dipendente["id"], dipendente["nome"], dipendente["cognome"], dipendente["data_nascita"],
                               dipendente["luogo_nascita"], dipendente["cf"], dipendente["telefono"], dipendente["ruolo"]))

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente_by_id(self, id):
        def is_selected_dipendente(dipendente):
            if dipendente.id == id:
                return True
            return False
        self.lista_dipendenti.remove(list(filter(is_selected_dipendente, self.lista_dipendenti))[0])

    def get_dipendente_by_index(self, index):
        return self.lista_dipendenti[index]

    def get_lista_dipendenti(self):
        return self.lista_dipendenti

    def save_data(self):
        with open('listadipendenti/data/lista_dipendenti.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)
