class GestorRestricciones:

    def __init__(self, rest):
        self.constraints = rest
        self.soft_const = self._set_constraints(2)
        self.hard_const = self._set_constraints(1)

    def evaluate_hard(self, estados):
        for e in estados:
            for r in self.hard_const:
                ...
            e.getevaluation()
        return estados

    def evaluate_soft(self, estados):
        for e in estados:
            e.getevaluation()
        return estados

    def _set_constraints(self, cont):
        list1 = []
        for i in self.constraints:
            if i.type1.value == cont:
                list1.append(i)
        return list1

