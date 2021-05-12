class ControlloreMenu():

    def __init__(self, menu):
        self.model = menu

    def get_prodotto(self):
        return self.model.prodotto

    def get_prezzo(self):
        return "{}".format(self.model.prezzo)

    def get_ingredienti(self):
        return self.model.ingredienti

    def get_isDisponibile(self):
        if self.model.disponibile:
            return "Disponibile"
        else:
            return "Non Disponibile"