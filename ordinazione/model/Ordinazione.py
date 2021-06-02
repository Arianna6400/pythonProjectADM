class Ordinazione:

    def __init__(self, tavolo, nome):
        super(Ordinazione, self).__init__()
        self.tavolo = tavolo
        self.nome = nome
        self.ordinazione = {}