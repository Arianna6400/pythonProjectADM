from unittest import TestCase

from listaordinazione.model.ListaOrdinazione import ListaOrdinazione
from prodotto.model.ProdottoSingolo import ProdottoSingolo
from listaordinazione.controller.ControlloreListaOrdinazione import ControlloreListaOrdinazione


class TestControlloreOrdinazione(TestCase):
    def setUp(self):
        self.lista = ListaOrdinazione()

    def test_aggiungi_ordinazione(self):    # test per controllare che l'ordinazione venga aggiunta correttamente
        d = {'Farina': '10'}
        self.test_prod = ProdottoSingolo("Pane", "2", d)
        self.lista.aggiungi_ordinazione(self.test_prod)
        self.assertIsNotNone(self.test_prod, "Non esiste")

    def test_ordinazione_vuota(self):   # test per verificare che la lista non sia vuota
        d = {'Farina': '10'}
        self.test_prod1 = ProdottoSingolo("Pane", "2", d)
        self.lista.aggiungi_ordinazione(self.test_prod1)
        self.assertNotEmpty(self.lista)

    def test_rimuovi_ordinazione(self):     # test per verificare la corretta eliminazione dell'ordinazione
        self.controller = ControlloreListaOrdinazione()
        d = {'Farina': '10'}
        self.test_prod2 = ProdottoSingolo("Pane", "2", d)
        self.controller.aggiungi_ordinazione(self.test_prod2)
        self.controller.elimina_ordinazione(0)
        self.assertEmpty(self.controller.get_lista_ordinazione())

    def test_change_disp(self):     # test per verificare il cambio di disponibilità del prodotto
        d = {'Farina': '10'}
        self.test_prod3 = ProdottoSingolo("Pane", "2", d)
        self.test_prod3.change_disp(False)
        self.assertFalse(self.test_prod3.disponibile, "Non è cambiata la disponibilità")

    def assertNotEmpty(self, obj):
        self.assertTrue(obj)

    def assertEmpty(self, obj):
        self.assertFalse(obj)
