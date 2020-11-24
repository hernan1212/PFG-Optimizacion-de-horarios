import enum


class tipoRest(enum.Enum):
    hard = 1
    soft = 2
    basic = 3

    def what_tipo(tipo):
        if tipo == 1:
            return tipoRest.hard
        elif tipo == 2:
            return tipoRest.soft
        return tipoRest.basic


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
    enumProfesor = "profesor"
    enumHora = "hora"
    enumAlumno = "estudiante"
    enumAula = "aula"
    enumAsignatura = "asignatura"
    enumAsigNombre = "asignatura.nombre"
    enumMaxAula = "aula.ocupacion"
    enumAsigClases = "asignatura.numClases"
    enumProfAptitudes = "profesor.aptitudes"
    enumAlumAptitudes = "estudiante.clases"
    enumHoraMax = "Relacion.HoraMax"
    enumDiaMax = "Relacion.DiaMax"

    def what_var(tipo):
        if tipo == "profesor":
            return varP.enumProfesor
        elif tipo == "hora":
            return varP.enumHora
        elif tipo == "estudiante":
            return varP.enumAlumno
        elif tipo == "aula":
            return varP.enumAula
        elif tipo == "asignatura":
            return varP.enumAsignatura
        elif tipo == "asignatura.nombre":
            return varP.enumAsigNombre
        elif tipo == "asignatura.numClases":
            return varP.enumAsigClases
        elif tipo == "HoraMax":
            return varP.enumHoraMax
        elif tipo == "DiaMax":
            return varP.enumDiaMax
        elif tipo == "estudiante.clases":
            return varP.enumAlumAptitudes
        elif tipo == "profesor.aptitudes":
            return varP.enumProfAptitudes
        elif tipo == "aula.ocupacion":
            return varP.enumMaxAula
        return tipo
