import os
import pickle


class ListaDipendenti():
    def __init__(self):
        super(ListaDipendenti, self).__init__()
        self.lista_dipendenti = []
        if os.path.isfile('listadipendenti/data/lista_dipendenti.pickle'):  # se esiste gia il file contenente i
            # dipendenti lo carica altrimenti lascia la lista vuota
            with open('listadipendenti/data/lista_dipendenti.pickle', 'rb') as f:
                self.lista_dipendenti = pickle.load(f)

    def aggiungi_dipendente(self, dipendente):  # metodo per aggiungere un dipendente alla lista
        self.lista_dipendenti.append(dipendente)

    def rimuovi_dipendente_by_id(self, id):  # metodo per rimuovere un dipendente dato il suo id
        def is_selected_dipendente(dipendente):
            if dipendente.id == id:
                return True
            return False

        self.lista_dipendenti.remove(list(filter(is_selected_dipendente, self.lista_dipendenti))[0])

    def get_dipendente_by_index(self, index):  # metodo che ritorna un dipendente dato l'indice
        return self.lista_dipendenti[index]

    def get_lista_dipendenti(self):  # metodo che ritorna la lista dei dipendenti
        return self.lista_dipendenti

    def save_data(self):  # metodo per salvare su file la lista dei dipendenti
        with open('listadipendenti/data/lista_dipendenti.pickle', 'wb') as handle:
            pickle.dump(self.lista_dipendenti, handle, pickle.HIGHEST_PROTOCOL)
