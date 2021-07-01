from prenotazione.model.Prenotazione import Prenotazione


class ControllorePrenotazione:
    def __init__(self, nome, telefono, num_persone, data):
        self.model = Prenotazione(nome, telefono, num_persone, data)

    def get_nome(self):
        return self.model.nome

    def get_telefono(self):
        return self.model.telefono

    def get_num_persone(self):
        return self.model.num_persone

    def get_data(self):
        return self.model.data

    def set_model(self, model):
        self.model = model
