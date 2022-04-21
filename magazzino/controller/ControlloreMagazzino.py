import os
import pickle

from magazzino.model.Magazzino import Magazzino


class ControlloreMagazzino:

    def __init__(self):
        super(ControlloreMagazzino, self).__init__()
        self.model = Magazzino()
        if os.path.isfile('magazzino/data/magazzino.pickle'):
            with open('magazzino/data/magazzino.pickle', 'rb') as f:
                self.model = pickle.load(f)

    def add_ingrediente(self, ingrediente, qt):
        if ingrediente in self.model.magazzino:
            self.model.magazzino[ingrediente] += qt
        else:
            self.model.magazzino[ingrediente] = qt

    def edit_ingrediente(self, ingrediente, qt):
        self.model.magazzino[ingrediente] = qt

    def get_magazzino(self):
        return self.model.magazzino

    def delete_ingrediente(self, index):
        keys = list(self.model.magazzino)
        return self.model.magazzino.pop(keys[index])

    def get_qt(self, ingrediente):
        return self.model.magazzino[ingrediente]

    def sort(self):
        sorted_dict = {}
        keys = sorted(self.model.magazzino.keys(), key=lambda x: x.lower())  # sort in ordine alfabetico e prende tutte le keys con la lettera minuscola

        for i in keys:
            values = self.model.magazzino[i]
            sorted_dict[i] = float(values)

        self.model.magazzino = sorted_dict

    def save_data(self):
        with open('magazzino/data/magazzino.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
