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

    def get_qt(self, ingrediente):
        return self.model.magazzino[ingrediente]

    def save_data(self):
        with open('magazzino/data/magazzino.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
