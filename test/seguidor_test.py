__author__ = 'javier'
import unittest
from modelo.seguidor import *


class TestsSeguidor(unittest.TestCase):

    def setUp(self):
        self.seguidor = Seguidor()
        self.seguidor.add_materia(Materia("Intro", 5))
        self.seguidor.add_materia(Materia("Orga", 10))

    def test_initialize(self):
        self.assertEquals(2, self.seguidor.count_materias())

    def test_add_materia(self):
        self.assertEquals(2, self.seguidor.count_materias())

    def test_average(self):
        self.assertEquals(7, self.seguidor.average())

    def test_best_note(self):
        self.assertEquals(10, self.seguidor.best_note())

    def test_note_materia(self):
        self.assertEquals(10, self.seguidor.note_materia("Orga"))

    def test_list_materia_aprobadas(self):
        self.assertEquals(1, len(self.seguidor.list_aprobadas()))

suite = unittest.TestLoader().loadTestsFromTestCase(TestsSeguidor)
unittest.TextTestRunner(verbosity=2).run(suite)