from AlgEjemplo import AlgEjemplo


class GestorProblema:

    @staticmethod
    def optimize(problem, rest):
        problem.strategy = AlgEjemplo(rest)
        result = problem.optimize()
        problem.result = result
