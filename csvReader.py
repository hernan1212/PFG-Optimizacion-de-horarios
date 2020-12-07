import pandas as pd
from LD.Estudiante import Estudiante
from LD.Profesor import Profesor
from LD.Asignatura import Asignatura
from LD.Aula import Aula
from LD.Restriccion import Restriccion
from LD.tipoRest import *


class csvReader:

    def __init__(self, log):
        self.log = log

    def readstudents(self, txt):
        dfAlumnos = pd.read_csv(txt)
        alumnos = list()
        if self.log: print("Lista de estudiantes")
        for i in range(0, len(dfAlumnos)):
            e = Estudiante(dfAlumnos.iloc[i, 0], dfAlumnos.iloc[i, 1], dfAlumnos.iloc[i, 2].split(','))
            alumnos.append(e)
            if self.log: alumnos[i].print_information()
        return alumnos

    def readprofessors(self, txt):
        dfProfesores = pd.read_csv(txt)
        profesores = list()
        if self.log: print("Lista de profesores")
        for i in range(0, len(dfProfesores)):
            p = Profesor(dfProfesores.iloc[i, 0], dfProfesores.iloc[i, 1], dfProfesores.iloc[i, 2].split(','))
            profesores.append(p)
            if self.log: profesores[i].print_information()
        return profesores

    def readsubjects(self, txt):
        dfAsignaturas = pd.read_csv(txt)
        asignaturas = list()
        if self.log: print("Lista de asignaturas")
        for i in range(0, len(dfAsignaturas)):
            a = Asignatura(dfAsignaturas.iloc[i, 0], dfAsignaturas.iloc[i, 1])

            asignaturas.append(a)
            if self.log: asignaturas[i].print_information()
        return asignaturas

    def readaulas(self, txt):
        dfAulas = pd.read_csv(txt)
        aulas = list()
        if self.log: print("Lista de aulas")
        for i in range(0, len(dfAulas)):
            a = Aula(dfAulas.iloc[i, 0], dfAulas.iloc[i, 1])
            aulas.append(a)
            if self.log: aulas[i].print_information()
        return aulas

    def readrestricciones(self, txt):
        dfRest = pd.read_csv(txt)
        restricciones = list()
        if self.log: print("Lista de Restricciones")
        for i in range(0, len(dfRest)):
            nombre = dfRest.iloc[i, 0]
            tipo = tipoRest.what_tipo(dfRest.iloc[i, 1])
            imp = importRest.what_import(dfRest.iloc[i, 2])
            contb = dfRest.iloc[i, 3].split(' ')
            cont = []
            for j in range(0, len(contb)):
                cont.append(varP.what_var(contb[j]))
            r = Restriccion(nombre, tipo, imp, cont, contb)
            restricciones.append(r)
            if self.log: restricciones[i].print_information()
        return restricciones
