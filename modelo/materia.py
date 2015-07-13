__author__ = 'javier'


class Materia:

    def __init__(self, name, note):
        self.name = name
        self.note = note
        self.aprobado = note >= 7

    def get_note(self):
        return self.note

    def get_name(self):
        return self.name

    def is_aprobada(self):
        return self.aprobado

    def is_name(self, name):
        return  self.name == name