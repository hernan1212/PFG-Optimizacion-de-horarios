from operator import attrgetter

from LD.Relacion import Relacion


class Estado:

    def __init__(self, indiv, alumnos, profesores, asignaturas, aulas):
        self.clases = []
        for i in range(0, indiv - 1):
            self.clases.append(Relacion(alumnos, profesores, asignaturas, aulas))

    def anadir_clases(self, clases):
        for c in clases:
            self.clases.append(c)

    def eliminar_clases(self, clases):
        for c in clases:
            self.clases.remove(c)

    def mutar(self):
        pass

    def desarrollar(self):
        pass

    def acotar(self):
        pass

    def print_result(self):
        cont = 1
        for c in self.clases:
            print("Clase" + str(cont) + ": " + str(c))
            cont += 1

    def getcost(self, action):
        cost = 0
        return cost

    def getevaluation(self):
        evaluation = 0
        return evaluation

    def isapplicable(self, action, problem):
        pass

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
