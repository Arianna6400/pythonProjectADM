from unittest import TestCase

from prenotazione.model.Prenotazione import Prenotazione
from prenotazione.controller.ControllorePrenotazione import ControllorePrenotazione
from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni

class TestControllorePrenotazione(TestCase):
    def setUp(self):
        self.controller = ControlloreListaPrenotazioni()
        self.moodel = ListaPrenotazioni()

    def test_aggiungi_prenotazione(self):
        self.test_prenotaz = Prenotazione("Davide", "3393876219", "20", "12/05/2022")
        self.controller.aggiungi_prenotazione(self.test_prenotaz)
        self.assertIsNotNone(self.test_prenotaz, "Non esiste")

    def test_lista_vuota(self):
        self.test_prenotaz1 = Prenotazione("Davide", "3393876219", "20", "12/05/2022")
        self.controller.aggiungi_prenotazione(self.test_prenotaz1)
        self.assertNotEmpty(self.controller)

    def test_elimina_prenotazione(self):        # non funziona
        self.test_prenotaz2 = Prenotazione("Davide", "3393876219", "20", "12/05/2022")
        print(self.test_prenotaz2.telefono)
        self.controller.aggiungi_prenotazione(self.test_prenotaz2)
        self.controller.elimina_prenotazione(self.test_prenotaz2)
        self.assertEmpty(self.controller.get_lista_prenotazione())

    def test_get_prenotazione_bydata(self):     # non funziona
        self.test_prenotaz3 = Prenotazione("Davide", "3393876219", "20", "12/05/2022")
        self.controller.aggiungi_prenotazione(self.test_prenotaz3)
        self.assertEqual(self.controller.get_prenotazioni_by_data("12/05/2022"), "12/05/2022")

    def assertNotEmpty(self, obj):
        self.assertTrue(obj)

    def assertEmpty(self, obj):
        self.assertFalse(obj)



