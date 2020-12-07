import math
import random
from abc import ABC
from GestorRestricciones import GestorRestricciones
from LD.Estado import Estado
from OptimizadorAlgoritmo import OptimizadorAlgoritmo


def print_estados(estados):
    for x in range(len(estados)):
        print("Estado" + str(x) + ": " + str(sum(estados[x].evalHard)))


class AlgEjemplo(OptimizadorAlgoritmo, ABC):
    indiv = 100
    crom = 0
    generations = 200
    comprobacionH = False
    comprobacionF = False

    def __init__(self, rest, logs):
        super().__init__(rest)
        self.gr = GestorRestricciones(rest, logs)
        self.logs = logs
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
            for j in i.clases:
                for k in asignaturas:
                    if k.nombre == j:
                        AlgEjemplo.crom += k.numClases
        self.gr.set_evaluations(AlgEjemplo.crom)
        for i in range(0, AlgEjemplo.indiv):
            estados.append(Estado(AlgEjemplo.crom, self.alum, self.prof, self.subj, self.rooms, self.horas))

        return estados

    def optimizar(self, estados):
        estados_c = estados
        nueva_generacion = [0 for x in range(0, len(estados_c))]

        for i in range(0, AlgEjemplo.generations):
            if self.logs: print("Iteracion numero " + str(i+1))
            indice_hijos = math.ceil(AlgEjemplo.indiv / 2)

            estados_h, AlgEjemplo.comprobacionH = self.gr.evaluate_hard(estados_c)
            # print_estados(estados_h)
            if AlgEjemplo.comprobacionH:
                estados_s, AlgEjemplo.comprobacionF = self.gr.evaluate_soft(estados_h.copy())
            else:
                estados_s = estados_h.copy()

            if AlgEjemplo.comprobacionH and AlgEjemplo.comprobacionF and len(estados_s) >= indice_hijos:
                print("El resultado es optimo!!!")
                return estados_h[0]

            if len(estados_s) < indice_hijos:

                for n in range(len(estados_s)):
                    nueva_generacion[n] = estados_s[n]

                for n in range(len(estados_s), indice_hijos):
                    nueva_generacion[n], k = estados_s[random.randint(0, len(estados_s) - 1)]. \
                        cruzar(estados_s[random.randint(0, len(estados_s) - 1)])
                    estados_s.append(k)
            else:
                for n in range(indice_hijos):
                    nueva_generacion[n] = estados_s[n]

            mutaciones = random.randint(0, indice_hijos)
            for j in range(mutaciones):
                nueva_generacion[random.randint(1, indice_hijos-1)].mutar(self.alum, self.prof, self.subj, self.rooms,
                                                                      self.horas)

            # nueva_generacion.sort(reverse=True, key=lambda x: x.evalSoft)
            # print(nueva_generacion[0].evalSoft)
            for k in range(0, indice_hijos, 2):
                nueva_generacion[indice_hijos], nueva_generacion[indice_hijos + 1] = estados_s[k].cruzar(
                  estados_s[k + 1])
                indice_hijos += 2

            estados_c = nueva_generacion.copy()

        print("No se ha podido llegar a un resultado optimo")
        return estados_c[0]
