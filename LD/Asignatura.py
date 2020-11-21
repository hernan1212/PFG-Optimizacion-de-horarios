class Asignatura:
    def __init__(self, nombre, numClases):
        self.nombre = nombre
        self.numClases = numClases
        self.necessities = []

    def print_information(self):
        print("Nombre: " + self.nombre + ", Clases: " + str(self.numClases))

    def __repr__(self):
        return self.nombre
