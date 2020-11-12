from abc import ABC
from GestorRestricciones import GestorRestricciones
from OptimizadorAlgoritmo import OptimizadorAlgoritmo


class AlgEjemplo(OptimizadorAlgoritmo, ABC):

    def __init__(self, rest):
        self.gr = GestorRestricciones(rest)

    def start_states(self, alumnos, profesores, asignaturas, aulas):
        # Inicializar estados

        estados = ""

        return estados

    def optimizar(self, estados):

        estados_c = []
        eval1 = self.gr.evaluate_hard(estados)
        eval2 = self.gr.evaluate_soft(estados)
        return estados_c
