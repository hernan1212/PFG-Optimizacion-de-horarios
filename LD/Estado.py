from operator import attrgetter
from random import randint
from varname import nameof
from LD.Relacion import Relacion
from LD.tipoRest import varP


class Estado:

    def __init__(self, indiv=0, alumnos=[], profesores=[], asignaturas=[], aulas=[]):
        self.clases = []
        self.evalHard = 0
        self.evalSoft = 0
        for i in range(0, indiv):
            self.clases.append(Relacion(alumnos, profesores, asignaturas, aulas))

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

    def mutar(self, alumnos, profesores, asignaturas, aulas):
        ind_mutado = randint(0, len(self.clases)-1)
        self.clases[ind_mutado] = Relacion(alumnos, profesores, asignaturas, aulas)

    def cruzar(self, estado2):
        ind_cruce = randint(0, len(self.clases))
        descendencia1 = Estado()
        descendencia2 = Estado()
        descendencia1.clases = self.clases[:ind_cruce] + estado2.clases[ind_cruce:]
        descendencia2.clases = self.clases[ind_cruce:] + estado2.clases[:ind_cruce]
        return descendencia1, descendencia2

    def print_result(self):
        cont = 1
        for c in self.clases:
            print("Clase" + str(cont) + ": " + str(c))
            cont += 1
        print("Evaluation: " + str(self.evalHard))

    def getevaluation(self):
        evaluation = 0
        return evaluation

    def effect(self, action):
        pass

    def repetitions(self, var1, var2):
        c = sorted(self.clases, key=attrgetter(var1, var2))

        key1 = 0
        it = 0
        rep = 0

        for i in c:
            if it == 1:
                key2 = i.key(var1, var2)
                if key1 == key2:
                    rep += 1
                key1 = key2
            else:
                key1 = i.key(var1, var2)
                it = 1

        return rep

    def comprobH(self, rest):
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
            if eval(" ".join(cont_b)):
                self.evalHard += 1

    def comprobS(self, rest):
        cont_a = [0 for x in rest.cont]
        cont_b = [0 for x in rest.cont]
        self.evalSoft = 0
        for i in self.clases:
            for j in range(len(rest.cont)):
                if isinstance(rest.cont[j], varP):
                    aux = i.get_var(rest.cont[j].value)
                    cont_a[j] = aux(i)
                    cont_b[j] = nameof(cont_a) + "[" + str(j) + "]"
                else:
                    cont_b[j] = str(rest.cont[j])
                self.evalSoft += exec(" ".join(cont_b))
