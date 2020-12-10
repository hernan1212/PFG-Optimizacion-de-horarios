from operator import attrgetter
from random import randint
from varname import nameof
from LD.Relacion import Relacion
from LD.tipoRest import varP


class Estado:

    repet = []
    evalTotalH = []
    evalTotalS = []

    def __init__(self, indiv=0, alumnos=[], profesores=[], asignaturas=[], aulas=[], horas=[]):
        self.clases = []
        self.clasesOK = []
        self.evalHard = []
        self.evalSoft = []
        for i in range(0, indiv):
            self.clases.append(Relacion(alumnos, profesores, asignaturas, aulas, horas))
            self.clasesOK.append(0)

    @property
    def evalHard(self):
        return self._evalHard

    @evalHard.setter
    def evalHard(self, evalHard):
        self._evalHard = evalHard

    @property
    def evalSoft(self):
        return self._evalSoft

    @evalSoft.setter
    def evalSoft(self, evalSoft):
        self._evalSoft = evalSoft

    def getid(self):
        a = 0
        for b in self.clases:
            a += b.getid()
        return a

    def mutar(self, alumnos, profesores, asignaturas, aulas, horas):
        f = True
        if self.clasesOK.count(self.clasesOK[0]) != len(self.clasesOK):
            while f:
                ind_mutado = randint(0, len(self.clases)-1)
                if self.clasesOK[ind_mutado] < 10:
                    self.clases[ind_mutado] = Relacion(alumnos, profesores, asignaturas, aulas, horas)
                    f = False
        else:
            ind_mutado = randint(0, len(self.clases)-1)
            self.clases[ind_mutado] = Relacion(alumnos, profesores, asignaturas, aulas, horas)

    def cruzar(self, estado2):
        ind_cruce = randint(0, len(self.clases))
        descendencia1 = Estado()
        descendencia2 = Estado()
        descendencia1.clases = self.clases[:ind_cruce] + estado2.clases[ind_cruce:]
        descendencia2.clases = self.clases[ind_cruce:] + estado2.clases[:ind_cruce]
        descendencia1.clasesOK = self.clasesOK[:ind_cruce] + estado2.clasesOK[ind_cruce:]
        descendencia2.clasesOK = self.clasesOK[ind_cruce:] + estado2.clasesOK[:ind_cruce]
        return descendencia1, descendencia2

    def print_result(self):
        cont = 1
        for c in self.clases:
            print("Clase" + str(cont) + ": " + str(c))
            cont += 1
        print("Evaluation Hard: ")
        for r in range(len(self.evalHard)):
            print("Rest " + str(r+1) + ": " + str(self.evalHard[r]))
        print("Evaluation Soft: ")
        for r in range(len(self.evalSoft)):
            print("Rest " + str(r+1) + ": " + str(self.evalSoft[r]))

    def getevaluation(self):
        evaluation = 0
        return evaluation

    def effect(self, action):
        pass

    def comprobH(self, rest, rnum):
        cont_a = [0 for x in rest.cont]
        cont_b = [0 for x in rest.cont]
        for i in range(len(self.clases)):
            for j in range(len(rest.cont)):
                if isinstance(rest.cont[j], varP):
                    aux = self.clases[i].get_var(rest.cont[j].value)
                    cont_a[j] = aux(self.clases[i])
                    cont_b[j] = nameof(cont_a) + "[" + str(j) + "]"
                else:
                    cont_b[j] = str(rest.cont[j])
            if eval(" ".join(cont_b)):
                self.evalHard[rnum] -= rest.risk.value
                self.clasesOK[i] += 1
        Estado.repet = []

    def comprobS(self, rest, rnum):
        cont_a = [0 for x in rest.cont]
        cont_b = [0 for x in rest.cont]
        for i in self.clases:
            for j in range(len(rest.cont)):
                if isinstance(rest.cont[j], varP):
                    aux = i.get_var(rest.cont[j].value)
                    cont_a[j] = aux(i)
                    cont_b[j] = nameof(cont_a) + "[" + str(j) + "]"
                else:
                    cont_b[j] = str(rest.cont[j])
            self.evalSoft[rnum] += eval(" ".join(cont_b))
        Estado.repet = []

def repetitions(var1):
    id1 = id(var1)
    Estado.repet.append(id1)
    return Estado.repet.count(id1)

def repetitions2(var1, var2):
    id1 = id(var1) + id(var2)
    Estado.repet.append(id1)
    return Estado.repet.count(id1)


def repetitions3(var1, var2, var3):
    id1 = id(var1) + id(var2) + id(var3)
    Estado.repet.append(id1)
    return Estado.repet.count(id1)


def repetitions3s(var1, var2, var3):
    id1 = id(var1) + id(var2) + id(var3)
    if Estado.repet.count(id1) == 1:
        return 1
    Estado.repet.append(id1)
    return 0




