__author__ = 'javier'
import unittest
from modelo.materia import *


class TestsMateria(unittest.TestCase):

    def setUp(self):
        self.orga = Materia("Orga", 5)

    def test_initialize(self):
        self.assertFalse(self.orga.is_aprobada())
        self.assertEquals(5, self.orga.get_note())
        self.assertEquals("Orga", self.orga.get_name())

suite = unittest.TestLoader().loadTestsFromTestCase(TestsMateria)
unittest.TextTestRunner(verbosity=2).run(suite)