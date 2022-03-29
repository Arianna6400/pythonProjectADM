import os
import pickle
from datetime import datetime

from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione
from magazzino.controller.ControlloreMagazzino import ControlloreMagazzino
from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class ControlloreOrdinazione:

    def __init__(self, ordinazione, menu):
        self.model = ordinazione
        self.menu = menu
        self.menu.update()

    def get_nome(self):
        return self.model.nome

    def get_tavolo(self):
        return self.model.tavolo

    def get_orario(self):
        return self.model.orario

    def get_ordinazione(self):
        return self.model.ordinazione

    def inserisci_prodotto(self, prodotto):
        magazzino = ControlloreMagazzino()
        if prodotto.get_isDisponibile() == "Disponibile":
            if prodotto.get_prodotto() in self.model.ordinazione:
                self.model.ordinazione[prodotto.get_prodotto()] += 1
            else:
                self.model.ordinazione[prodotto.get_prodotto()] = 1

            for ingrediente, qt in prodotto.get_ingredienti().items():
                magazzino.add_ingrediente(ingrediente, -float(qt))

            self.menu.update()
            magazzino.save_data()

            return True
        return False

    def elimina_ordinazione(self):
        magazzino = ControlloreMagazzino()
        for prodotto, qt in self.model.ordinazione.items():
            for alimento in self.menu.get_lista_menu():
                controllore_alimento = ControlloreProdotto(alimento)
                if controllore_alimento.get_prodotto() == prodotto:
                    for ingrediente, qt2 in controllore_alimento.get_ingredienti().items():
                        magazzino.add_ingrediente(ingrediente, float(qt2 * qt))

        magazzino.save_data()
        self.menu.update()
        self.model.ordinazione = {}

    def conferma_ordinazione(self):
        self.model.orario = datetime.now().strftime("%H:%M:%S")
        lista_ordinazione = ControlloreListaOrdinazione()

        lista_ordinazione.aggiungi_ordinazione(self)
        lista_ordinazione.save_data()
