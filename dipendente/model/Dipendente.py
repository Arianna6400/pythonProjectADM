class Dipendente():
    def __init__(self, id, nome, cognome, data_nascita, luogo_nascita, cf, telefono, ruolo):
        super(Dipendente, self).__init__()
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.cf = cf
        self.telefono = telefono
        self.ruolo = ruolo