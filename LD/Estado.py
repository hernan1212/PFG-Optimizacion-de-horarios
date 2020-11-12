from operator import attrgetter

class Estado:
    def __init__(self, clases):
        self.clases = clases


    def anadir_clases(self, clases):
        for c in clases:
            self.clases.append(c)

    def eliminar_clases(self, clases):
        for c in clases:
            self.clases.delete(c)

    def mutar(self):
        pass

    def desarrollar(self):
        pass

    def acotar(self):
        pass

    def print_result(self):
        pass

    def getcost(self, action):
        cost = 0
        return cost

    def getevaluation(self, problem):
        evaluation = 0
        return evaluation

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
                key1 == key2
            else:
                key1 = i.key(var1, var2)
                it = 1

        return rep

