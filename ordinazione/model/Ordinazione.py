class Ordinazione:

    def __init__(self, nome, tavolo):
        super(Ordinazione, self).__init__()
        self.tavolo = tavolo
        self.nome = nome
        self.orario = 00
        self.ordinazione = {}
