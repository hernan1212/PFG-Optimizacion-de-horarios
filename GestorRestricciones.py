import AlgEjemplo
from LD.Estado import Estado
from LD.Relacion import Relacion


class GestorRestricciones:

    def __init__(self, rest, logs):
        self.constraints = rest
        self.hardEval = 0
        self.softEval = 0
        self.repes = []
        self.basic_const = self._set_constraints(3)
        self.soft_const = self._set_constraints(2)
        self.hard_const = self._set_constraints(1)
        self.logs = logs
        self._set_basic_param()

    def evaluate_hard(self, estados):
        repes = list()
        for e in reversed(range(len(estados))):
            estados[e].evalHard = Estado.evalTotalH.copy()
            for r in range(len(self.hard_const)):
                estados[e].comprobH(self.hard_const[r], r)
            if (sum(estados[e].evalHard) > self.hardEval) and (len(estados) > 2):
                estados.pop(e)
            elif hash(estados[e]) in self.repes and len(estados) > 2:
                estados.pop(e)
            else:
                repes.append(hash(estados[e]))
        estados.sort(key=lambda x: sum(x.evalHard))
        if sum(estados[0].evalHard) < self.hardEval:
            self.hardEval = sum(estados[0].evalHard)
        if self.logs: print("Mejor evaluación restricciones duras: " + str(sum(estados[0].evalHard)))
        if self.logs: print("Numero de individuos que lo cumplen: " + str(len(estados)))
        if self.hardEval == 0:
            return estados, True

        return estados, False

    def evaluate_soft(self, estados):
        for e in reversed(range(len(estados))):
            estados[e].evalSoft = Estado.evalTotalS.copy()
            for r in range(len(self.soft_const)):
                estados[e].comprobS(self.soft_const[r], r)
                if (sum(estados[e].evalSoft) < self.softEval) and (len(estados) > 2):
                    estados.pop(e)
        estados.sort(reverse=True, key=lambda x: sum(x.evalSoft))
        if self.logs: print("Mejor evaluación restricciones suaves: " + str(sum(estados[0].evalSoft)))
        if self.logs: print("Numero de individuos que lo cumplen: " + str(len(estados)))
        if sum(estados[0].evalSoft) > self.softEval:
            self.softEval = sum(estados[0].evalSoft)
            return estados, False
        return estados, True

    def _set_constraints(self, cont):
        list1 = []
        for i in self.constraints:
            if i.type1.value == cont:
                list1.append(i)
        return list1

    def _set_basic_param(self):
        for i in self.basic_const:
            exec(" ".join(i.cont_b))

    def set_evaluations(self, crom):
        Estado.evalTotalH = [0 for x in range(len(self.hard_const))]
        for e in range(len(Estado.evalTotalH)):
            Estado.evalTotalH[e] = self.hard_const[e].risk.value * crom
        self.hardEval = sum(Estado.evalTotalH)/2
        Estado.evalTotalS = [0 for x in range(len(self.soft_const))]
        self.softEval = 0

