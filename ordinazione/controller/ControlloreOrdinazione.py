class ControlloreOrdinazione:

    def __init__(self, ordinazione):
        self.model = ordinazione

    def get_ordinazione(self):
        return self.model

    def inserisci_ordinazione(self, prodotto):
        if prodotto.prodotto in self.model.ordinazione:
            self.model.ordinazione[prodotto.prodotto] += 1
        else:
            self.model.ordinazione[prodotto.prodotto] = 1

    def elimina_ordinazione(self, prodotto):
        if prodotto.prodotto in self.model.ordinazione:
            del self.model.ordinazione[prodotto.prodotto]

    def elimina_ordinazione(self):
        self.model.ordinazione = {}
