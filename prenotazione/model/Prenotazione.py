class Prenotazione:

    def __init__(self, nome, telefono, num_persone, data):
        super(Prenotazione, self).__init__()
        self.nome = nome
        self.telefono = telefono
        self.num_persone = num_persone
        self.data = data
