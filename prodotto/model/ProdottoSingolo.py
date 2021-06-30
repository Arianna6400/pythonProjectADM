class ProdottoSingolo:

    def __init__(self, prodotto, prezzo, ingredienti):
        super(ProdottoSingolo, self).__init__()
        self.prodotto = prodotto
        self.prezzo = prezzo
        self.ingredienti = ingredienti
        self.disponibile = True

    def change_disp(self, b):
        self.disponibile = b

