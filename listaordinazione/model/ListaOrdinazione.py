
class ListaOrdinazione:

    def __init__(self):
        super(ListaOrdinazione, self).__init__()
        self.lista_ordinazione = []

    def aggiungi_ordinazione(self, ordinazione):
        self.lista_ordinazione.append(ordinazione)

    def elimina_ordinazione(self, index):
        self.lista_ordinazione.remove(self.lista_ordinazione[index])

    def get_ordinazione_by_index(self, index):
        return self.lista_ordinazione[index]

    def get_lista_ordinazione(self):
        return self.lista_ordinazione
