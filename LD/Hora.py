class Hora:
    idAct = 1

    def __init__(self, hora, dia):
        self.id = Hora.idAct
        self.hora = hora
        self.dia = dia
        Hora.idAct += 1

    def print_information(self):
        print("Hora: " + str(self.hora) + "Dia: " + str(self.dia))

    def __repr__(self):
        return str(self.id)