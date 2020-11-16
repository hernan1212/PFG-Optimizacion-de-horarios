from LD.Persona import Persona


class Profesor(Persona):
    def __init__(self, nombre, apellido, aptitudes):
        Persona.__init__(self, nombre, apellido)
        self.aptitudes = aptitudes  # Lista de aptitudes que tiene un profesor

    def print_information(self):
        print("Nombre: " + self.nombre + ", Apellido: " + self.apellido + ", Asignaturas: " + ','.join(self.aptitudes))

    def __repr__(self):
        return self.nombre
