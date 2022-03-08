from unittest import TestCase

from dipendente.model.Dipendente import Dipendente
from listadipendenti.controller.ControlloreListaDipendenti import ControlloreListaDipendenti
from listadipendenti.model.ListaDipendenti import ListaDipendenti


class TestControlloreDipendente(TestCase):

    def setUp(self):
        self.lista = ListaDipendenti()

    def test_aggiungi_dipendente(self):     # test per controllare che il dipendente venga aggiunto correttamente
        self.test_dip = Dipendente("MarioRossi", "Mario", "Rossi", "12/02/1989", "Rimini", "mrirss00msdk123m", "3391023457", "Cameriere")
        self.lista.aggiungi_dipendente(self.test_dip)
        self.assertIsNotNone(self.test_dip, "Non esiste")

    def test_controlla_dipendente(self):    # test per confrontare l'uguaglianza tra due dipendenti
        self.test_dip1 = Dipendente("MarioRossi", "Mario", "Rossi", "12/02/1989", "Rimini", "mrirss00msdk123m", "3391023457", "Cameriere")
        self.test_dip2 = Dipendente("MarioRossi", "Mario", "Rossi", "12/02/1989", "Rimini", "mrirss00msdk123m", "3391023457", "Cameriere")
        self.assertNotEqual(self.test_dip1, self.test_dip2, "Dipendente già esistente")

    def test_lista_vuota(self):     # test per verificare che la lista non sia vuota
        self.test_dip3 = Dipendente("MarioRossi", "Mario", "Rossi", "12/02/1989", "Rimini", "mrirss00msdk123m", "3391023457", "Cameriere")
        self.lista.aggiungi_dipendente(self.test_dip3)
        self.assertNotEmpty(self.lista)

    def test_elimina_dipendente(self):      # test per verificare che il dipendente venga rimosso correttamente dalla lista
        self.controller = ControlloreListaDipendenti()
        self.test_dip4 = Dipendente("MarioRossi", "Mario", "Rossi", "12/02/1989", "Rimini", "mrirss00msdk123m", "3391023457", "Cameriere")
        self.controller.aggiungi_dipendente(self.test_dip4)
        self.controller.elimina_dipendente_by_id("MarioRossi")
        self.assertEmpty(self.controller.get_lista_dipendenti())

    def assertNotEmpty(self, obj):
        self.assertTrue(obj)

    def assertEmpty(self, obj):
        self.assertFalse(obj)
