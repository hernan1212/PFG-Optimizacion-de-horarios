from OptimizadorAlgoritmo import OptimizadorAlgoritmo


class Problem:

    def __init__(self):
        self.restricciones = ""
        self.name = ""

    def __str__(self):
        return "..."

    @property
    def strategy(self):

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: OptimizadorAlgoritmo):
        self._strategy = strategy

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        self._result = result

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, states):
        self._states = states

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        self._students = students

    @property
    def professors(self):
        return self._professors

    @professors.setter
    def professors(self, professors):
        self._professors = professors

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, subjects):
        self._subjects = subjects

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        self._rooms = rooms

    def set_restricciones(self, restricciones):
        pass

    def optimize(self):
        self._states = self.strategy.start_states(self._students, self._professors, self._subjects, self._rooms)
        return self.strategy.optimizar(self._states)







