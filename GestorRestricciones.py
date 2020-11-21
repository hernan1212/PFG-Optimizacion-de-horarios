from LD.Relacion import Relacion


class GestorRestricciones:

    def __init__(self, rest):
        self.constraints = rest
        self.basic_const = self._set_constraints(3)
        self.soft_const = self._set_constraints(2)
        self.hard_const = self._set_constraints(1)
        self._set_basic_param()

    def evaluate_hard(self, estados):
        for e in estados:
            e.evalHard = 0
            for r in self.hard_const:
                e.comprobH(r)
        estados.sort(reverse=True, key=lambda x: x.evalHard)
        return estados

    def evaluate_soft(self, estados):
        for e in estados:
            for r in self.soft_const:
                e.comprobS(r)
        return estados

    def _set_constraints(self, cont):
        list1 = []
        for i in self.constraints:
            if i.type1.value == cont:
                list1.append(i)
        return list1

    def _set_basic_param(self):
        for i in self.basic_const:
            exec(" ".join(i.cont_b))
