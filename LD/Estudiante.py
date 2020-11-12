from LD.Persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre, apellido, asig):
        Persona.__init__(self, nombre, apellido)

        self.clases = asig  # Lista de clases a las que tiene un estudiante

    def print_information(self):
        print("Nombre: " + self.nombre + ", Apellido: " + self.apellido + ", Asignaturas: " + ','.join(self.clases))
