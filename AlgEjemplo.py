from abc import ABC
from GestorRestricciones import GestorRestricciones
from LD.Estado import Estado
from OptimizadorAlgoritmo import OptimizadorAlgoritmo


class AlgEjemplo(OptimizadorAlgoritmo, ABC):

    def __init__(self, rest):
        self.gr = GestorRestricciones(rest)

    def start_states(self, alumnos, profesores, asignaturas, aulas):
        # Inicializar estados
        germ = 10
        indiv = 10
        estados = []
        for i in range(1, germ):
            estados.append(Estado(indiv, alumnos, profesores, asignaturas, aulas))

        return estados

    def optimizar(self, estados):

        estados_c = estados
        eval1 = self.gr.evaluate_hard(estados)
        eval2 = self.gr.evaluate_soft(estados)
        return estados_c[0]
