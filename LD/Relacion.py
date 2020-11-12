from operator import attrgetter

class Relacion:
    def __init__(self, profesor, estudiante, asignatura, aula, hora):
        self.profesor = profesor
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.aula = aula
        self.hora = hora

    def key(self, var1, var2):
        return attrgetter(var1) + attrgetter(var2)
