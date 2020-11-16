class Aula:

    def __init__(self, nombre, ocupacion):
        self.nombre = nombre
        self.recursos = []
        self.ocupacion = ocupacion

    def print_information(self):
        print("Nombre: " + str(self.nombre) + ", Ocupacion Max: " + str(self.ocupacion) + " personas")

    def __repr__(self):
        return str(self.nombre)
