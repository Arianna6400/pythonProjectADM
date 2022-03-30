from unittest import TestCase
from datetime import timedelta
import datetime

from prenotazione.model.Prenotazione import Prenotazione
from listaprenotazioni.model.ListaPrenotazioni import ListaPrenotazioni
from listaprenotazioni.controller.ControlloreListaPrenotazioni import ControlloreListaPrenotazioni


class TestControllorePrenotazione(TestCase):
    def setUp(self):
        self.controller = ControlloreListaPrenotazioni()
        self.model = ListaPrenotazioni()

    def test_aggiungi_prenotazione(self):
        data = datetime.datetime(2022, 5, 12)
        new_data = data + timedelta(hours=int(12)) + timedelta(minutes=int(30))
        print(data)
        print(new_data)
        print(self.model.lista_prenotazioni)
        # self.test_prenotaz = Prenotazione("Davide", "3393876219", "20", new_data)
        # self.controller.aggiungi_prenotazione(self.test_prenotaz)
        self.controller.aggiungi_prenotazione(Prenotazione("Davide", "3393901914", "20", new_data))
        print(self.model.lista_prenotazioni)
        # self.assertIsNotNone(self.test_prenotaz, "Non esiste")

    def test_lista_vuota(self):
        data = datetime.datetime(2022, 5, 12)
        self.test_prenotaz1 = Prenotazione("Davide", "3393876219", "20", data)
        self.controller.aggiungi_prenotazione(self.test_prenotaz1)
        self.assertNotEmpty(self.controller.get_lista_prenotazione())

    def test_elimina_prenotazione(self):
        data = datetime.datetime(2022, 5, 12)
        self.test_prenotaz2 = Prenotazione("Davide", "3393876219", "20", data)
        print(self.test_prenotaz2.telefono)
        self.controller.aggiungi_prenotazione(self.test_prenotaz2)
        self.controller.elimina_prenotazione(self.test_prenotaz2)
        self.assertEmpty(self.controller.get_lista_prenotazione())

    def test_get_prenotazione_bydata(self):
        data = datetime.datetime(2022, 5, 12)
        self.test_prenotaz3 = Prenotazione("Davide", "3393876219", "20", data.date())
        self.controller.aggiungi_prenotazione(self.test_prenotaz3)
        self.assertEqual(self.controller.get_prenotazioni_by_data(data.date()), "2022-05-12")

    def assertNotEmpty(self, obj):
        self.assertTrue(obj)

    def assertEmpty(self, obj):
        self.assertFalse(obj)
