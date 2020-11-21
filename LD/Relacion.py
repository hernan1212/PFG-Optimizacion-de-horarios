from operator import attrgetter
from random import randint


class Relacion:
    HorasMax = 0
    DiasMax = 0

    def __init__(self, alumnos, profesores, asignaturas, aulas):
        self.profesor = profesores[randint(0, len(profesores)-1)]
        self.estudiante = alumnos[randint(0, len(alumnos) - 1)]
        self.asignatura = asignaturas[randint(0, len(asignaturas) - 1)]
        self.aula = aulas[randint(0, len(aulas) - 1)]
        self.hora = randint(1, Relacion.HorasMax)
        self.dia = randint(1, Relacion.DiasMax)

    def __repr__(self):
        return "Prof: " + str(self.profesor) + " Estud: " + str(self.estudiante) + " Asig: " + str(self.asignatura) \
               + " Aula: " + str(self.aula) + " Hora: " + str(self.hora) + " Dia: " + str(self.dia)

    def key(self, var1, var2):
        return str(attrgetter(var1)) + str(attrgetter(var2))

    def get_var(self, var):
        return attrgetter(var)
