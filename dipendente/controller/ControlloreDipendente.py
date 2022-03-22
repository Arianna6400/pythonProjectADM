class ControlloreDipendente():
    def __init__(self, dipendente):
        self.model = dipendente

    def get_id_dipendente(self):
        return self.model.id

    def get_nome_dipendente(self):
        return self.model.nome

    def get_cognome_dipendente(self):
        return self.model.cognome

    def get_cf_dipendente(self):
        return self.model.cf

    def get_data_nascita_dipendente(self):
        return self.model.data_nascita

    def get_luogo_nascita_dipendente(self):
        return self.model.luogo_nascita

    def get_telefono_dipendente(self):
        return self.model.telefono

    def get_ruolo_dipendente(self):
        return self.model.ruolo