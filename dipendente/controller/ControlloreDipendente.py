from dipendente.model.Dipendente import Dipendente


class ControlloreDipendente:
    def __init__(self, codice_identificativo, nome, cognome, data_nascita, luogo_nascita, cf, telefono, ruolo):
        self.model = Dipendente(codice_identificativo, nome, cognome, data_nascita, luogo_nascita, cf, telefono, ruolo)

    def get_id_dipendente(self):
        return self.model.get_id_dipendente()

    def get_nome_dipendente(self):
        return self.model.get_nome_dipendente()

    def get_cognome_dipendente(self):
        return self.model.get_cognome_dipendente()

    def get_cf_dipendente(self):
        return self.model.get_cf_dipendente()

    def get_data_nascita_dipendente(self):
        return self.model.get_data_nascita_dipendente()

    def get_luogo_nascita_dipendente(self):
        return self.model.get_luogo_nascita_dipendente()

    def get_telefono_dipendente(self):
        return self.model.get_telefono_dipendente()

    def get_ruolo_dipendente(self):
        return self.model.get_ruolo_dipendente()
