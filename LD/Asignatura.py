class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.necessities = []

    def print_information(self):
        print("Nombre: " + self.nombre)
