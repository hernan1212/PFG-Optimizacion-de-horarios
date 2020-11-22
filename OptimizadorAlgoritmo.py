from abc import abstractmethod, ABC


class OptimizadorAlgoritmo(ABC):

    @abstractmethod
    def __init__(self, rest):
        pass

    @abstractmethod
    def start_states(self, alumnos, profesores, asignaturas, aulas, horas):
        pass

    @abstractmethod
    def optimizar(self, estados):
        pass
