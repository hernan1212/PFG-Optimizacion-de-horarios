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
    indiv = 100
    crom = 0
    generations = 5

    def __init__(self, rest):
        super().__init__(rest)
        self.gr = GestorRestricciones(rest)
        self.alum = []
        self.prof = []
        self.subj = []
        self.rooms = []
        self.horas = []

    def start_states(self, alumnos, profesores, asignaturas, aulas, horas):
        # Inicializar estados
        self.alum = alumnos
        self.prof = profesores
        self.subj = asignaturas
        self.rooms = aulas
        self.horas = horas

        estados = []
        for i in alumnos:
            AlgEjemplo.crom += len(i.clases)
        for i in range(0, AlgEjemplo.indiv):
            estados.append(Estado(AlgEjemplo.crom, self.alum, self.prof, self.subj, self.rooms, self.horas))

        return estados

    def optimizar(self, estados):
        estados_c = estados
        nueva_generacion = [0 for x in range(0, len(estados_c))]

        for i in range(0, AlgEjemplo.generations):
            indice_hijos = math.ceil(AlgEjemplo.indiv / 2)

            estados_h = self.gr.evaluate_hard(estados_c)
            # print_estados(estados_h)
            if len(estados_h) < indice_hijos:

                for n in range(len(estados_h)):
                    nueva_generacion[n] = estados_h[n]

                for n in range(len(estados_h), indice_hijos):
                    nueva_generacion[n], k = estados_h[random.randint(0, len(estados_h) - 1)]. \
                        cruzar(estados_h[random.randint(0, len(estados_h) - 1)])
                    estados_h.append(k)
            else:
                for n in range(indice_hijos):
                    nueva_generacion[n] = estados_h[n]

            # print(nueva_generacion[0].evalHard)
            for k in range(0, indice_hijos, 2):
                nueva_generacion[indice_hijos], nueva_generacion[indice_hijos + 1] = estados_h[k].cruzar(
                    estados_h[k + 1])
                indice_hijos += 2

            indice_hijos = math.ceil(AlgEjemplo.indiv / 2)
            estados_s = self.gr.evaluate_soft(nueva_generacion)

            for n in range(0, indice_hijos):
                nueva_generacion[n] = estados_s[n]
            mutaciones = random.randint(0, indice_hijos / 2)
            for j in range(0, mutaciones):
                nueva_generacion[random.randint(0, mutaciones)].mutar(self.alum, self.prof, self.subj, self.rooms,
                                                                      self.horas)
            nueva_generacion.sort(reverse=True, key=lambda x: x.evalSoft)
            # print(nueva_generacion[0].evalSoft)
            for k in range(0, indice_hijos, 2):
                nueva_generacion[indice_hijos], nueva_generacion[indice_hijos + 1] = estados_s[k].cruzar(
                  estados_s[k + 1])
                indice_hijos += 2

            estados_c = nueva_generacion.copy()

        return estados_c[0]
