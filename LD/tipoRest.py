import enum


class tipoRest(enum.Enum):
    soft = 1
    hard = 2

    def what_tipo(tipo):
        if tipo == 1:
            return tipoRest.soft
        return tipoRest.hard

class importRest(enum.Enum):
    high = 1
    medium = 2
    low = 3

    def what_import(tipo):
        if tipo == 1:
            return importRest.high
        elif tipo == 2:
            return importRest.medium
        return importRest.low


class varP(enum.Enum):
    enumProfesor = "Profesor"
    enumHora = "Hora"
    enumAlumno = "Alumno"
    enumAula = "Aula"
    enumAsignatura = "Asignatura"
    enumMaxAula = "MaxAula"

    def what_var(tipo):
        if tipo == "Profesor":
            return varP.enumProfesor
        elif tipo == "Hora":
            return varP.enumHora
        elif tipo == "Alumno":
            return varP.enumAlumno
        elif tipo == "Aula":
            return varP.enumAula
        elif tipo == "Asignatura":
            return varP.enumAsignatura
        return varP.enumMaxAula

