class Dipendente:
    def __init__(self, codice_identificativo, nome, cognome, data_nascita, luogo_nascita, cf, telefono, ruolo):
        super(Dipendente, self).__init__()
        self.codice_identificativo = codice_identificativo
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.cf = cf
        self.telefono = telefono
        self.ruolo = ruolo

    def get_id_dipendente(self):
        return self.codice_identificativo

    def get_nome_dipendente(self):
        return self.nome

    def get_cognome_dipendente(self):
        return self.cognome

    def get_cf_dipendente(self):
        return self.cf

    def get_data_nascita_dipendente(self):
        return self.data_nascita

    def get_luogo_nascita_dipendente(self):
        return self.luogo_nascita

    def get_telefono_dipendente(self):
        return self.telefono

    def get_ruolo_dipendente(self):
        return self.ruolo
