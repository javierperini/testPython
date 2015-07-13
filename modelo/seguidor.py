__author__ = 'javier'
from materia import *


class Seguidor:

    def __init__(self):
        self.list_materias = []

    def count_materias(self):
        return self.list_materias.__len__()

    def add_materia(self, materia):
        self.list_materias.append(materia)

    def average(self):
        average = 0
        for materia in self.list_materias:
            average = average + materia.get_note()
        return average/self.count_materias()

    def best_note(self):
        return max(self.list_materias, key=lambda materia: materia.get_note()).get_note()

    def note_materia(self, name):
        res = list(filter((lambda x: x.is_name(name)), self.list_materias))
        return res.pop().get_note()

    def list_aprobadas(self):
        return list(filter((lambda x: x.is_aprobada()), self.list_materias))

