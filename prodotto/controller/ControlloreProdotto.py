class ControlloreProdotto():

    def __init__(self, prodotto):
        self.model = prodotto

    def get_prodotto(self):
        return self.model.prodotto

    def get_prezzo(self):
        return "{}".format(self.model.prezzo)

    def get_ingredienti(self):
        return self.model.ingredienti

    def change_disp(self, b):
        self.model.disponibile = b

    def get_isDisponibile(self):
        if self.model.disponibile:
            return "Disponibile"
        else:
            return "Non Disponibile"
