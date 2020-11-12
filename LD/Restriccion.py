class Restriccion:
    def __init__(self, name, type1, risk, cont, cont_b):
        self.name = name
        self.type1 = type1
        self.risk = risk
        self.cont = cont
        self.cont_b = cont_b

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def type1(self):
        return self._type1

    @type1.setter
    def type1(self, type1):
        self._type1 = type1

    @property
    def risk(self):
        return self._risk

    @risk.setter
    def risk(self, risk):
        self._risk = risk

    @property
    def cont(self):
        return self._cont

    @cont.setter
    def cont(self, cont):
        self._cont = cont

    @property
    def cont_b(self):
        return self._cont_b

    @cont_b.setter
    def cont_b(self, cont_b):
        self._cont_b = cont_b

    def print_information(self):
        print("Nombre: " + str(self._name) + ", tipo: " + self._type1.name + ", importancia: "
              + self.risk.name + ", contenido: " + " ".join(self._cont_b))
