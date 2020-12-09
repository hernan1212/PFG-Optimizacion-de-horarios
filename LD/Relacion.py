from operator import attrgetter
from random import randint


class Relacion:
    HorasMax = 0
    DiasMax = 0

    def __init__(self, alumnos, profesores, asignaturas, aulas, horas):
        self.profesor = profesores[randint(0, len(profesores)-1)]
        self.estudiante = alumnos[randint(0, len(alumnos) - 1)]
        self.asignatura = asignaturas[randint(0, len(asignaturas) - 1)]
        self.aula = aulas[randint(0, len(aulas) - 1)]
        self.hora = horas[randint(0, len(horas) - 1)]

    def __repr__(self):
        return "Prof: " + str(self.profesor) + " Estud: " + str(self.estudiante) + " Asig: " + str(self.asignatura) \
               + " Aula: " + str(self.aula) + " Hora: " + str(self.hora)

    def get_var(self, var):
        return attrgetter(var)

    def getid(self):
        return id(self.profesor) + id(self.estudiante) + id(self.asignatura) + id(self.aula) + id(self.hora)
