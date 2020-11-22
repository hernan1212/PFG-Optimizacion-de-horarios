import AlgEjemplo
from LD.Relacion import Relacion


class GestorRestricciones:

    def __init__(self, rest):
        self.constraints = rest
        self.hardTotal = 0
        self.hardEval = 5
        self.softTotal = 0
        self.basic_const = self._set_constraints(3)
        self.soft_const = self._set_constraints(2)
        self.hard_const = self._set_constraints(1)
        self._set_basic_param()

    def evaluate_hard(self, estados):
        for e in reversed(range(len(estados))):
            estados[e].evalHard = 0
            self.hardTotal = 0
            for r in self.hard_const:
                estados[e].comprobH(r)
                self.hardTotal += len(estados[e].clases) * r.risk.value
            if self.hardTotal-estados[e].evalHard > self.hardEval:
                estados.pop(e)
        estados.sort(reverse=True, key=lambda x: x.evalHard)
        if self.hardTotal-estados[0].evalHard < self.hardEval:
            self.hardEval = self.hardTotal-estados[0].evalHard

        return estados

    def evaluate_soft(self, estados):
        for e in estados:
            e.evalSoft = 0
            self.softTotal = 0
            for r in self.soft_const:
                e.comprobS(r)
                self.softTotal += len(e.clases) * r.risk.value
        estados.sort(reverse=True, key=lambda x: x.evalSoft)
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
