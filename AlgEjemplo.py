import math
import random
from abc import ABC
from GestorRestricciones import GestorRestricciones
from LD.Estado import Estado
from OptimizadorAlgoritmo import OptimizadorAlgoritmo


def print_estados(estados):
    for x in range(len(estados)):
        print("Estado" + str(x) + ": " + str(estados[x].evalHard))


class AlgEjemplo(OptimizadorAlgoritmo, ABC):

    def __init__(self, rest):
        super().__init__(rest)
        self.gr = GestorRestricciones(rest)
        self.alum = []
        self.prof = []
        self.subj = []
        self.rooms = []
        self.indiv = 20
        self.crom = 0
        self.generations = 7

    def start_states(self, alumnos, profesores, asignaturas, aulas):
        # Inicializar estados
        self.alum = alumnos
        self.prof = profesores
        self.subj = asignaturas
        self.rooms = aulas
        self.crom = 0
        estados = []
        for i in alumnos:
            self.crom += len(i.clases)
        for i in range(0, self.indiv):
            estados.append(Estado(self.crom, self.alum, self.prof, self.subj, self.rooms))

        return estados

    def optimizar(self, estados):
        estados_c = estados
        nueva_generacion = [Estado() for x in range(0, len(estados_c))]

        for i in range(0, self.generations):
            indice_hijos = math.ceil(self.indiv / 2)

            estados_h = self.gr.evaluate_hard(estados_c)
            print_estados(estados_h)
            estados_s = self.gr.evaluate_soft(estados_c)

            for n in range(0, indice_hijos):
                nueva_generacion[n] = estados_h[n]

            mutaciones = random.randint(0, indice_hijos-1)
            for j in range(0, mutaciones):
                nueva_generacion[random.randint(0, mutaciones)].mutar(self.alum, self.prof, self.subj, self.rooms)

            for k in range(0, indice_hijos, 2):
                nueva_generacion[indice_hijos], nueva_generacion[indice_hijos + 1] = estados_h[k].cruzar(
                    estados_c[k + 1])
                indice_hijos += 2

            estados_c = nueva_generacion

        return estados_c[0]
