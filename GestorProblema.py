from AlgEjemplo import AlgEjemplo
from LD.Asignatura import Asignatura
from LD.Aula import Aula
from LD.Persona import Persona
from LD.Estudiante import Estudiante
from LD.Profesor import Profesor
from LD.Relacion import Relacion
from LD.Estado import Estado
from LD.Problem import Problem
from GestorRestricciones import GestorRestricciones as gr


class GestorProblema:


    @staticmethod
    def optimize(problem, rest):
        problem.strategy = AlgEjemplo(rest)
        result = problem.optimize()
        problem.result = result


    @staticmethod
    def isapplicable(state, action, problem):
        value = True
        return value

    @staticmethod
    def effect(state, action):
        result = ...
        return ...





