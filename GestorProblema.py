from AlgEjemplo import AlgEjemplo
from LD.Relacion import Relacion
from LD.Hora import Hora


class GestorProblema:

    @staticmethod
    def optimize(problem, rest, logs):
        problem.strategy = AlgEjemplo(rest, logs)

        horas = []
        for i in range(Relacion.DiasMax):
            for j in range(Relacion.HorasMax):
                horas.append(Hora(j, i))
        problem.horas = horas

        result = problem.optimize()
        problem.result = result
