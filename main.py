#!/usr/bin/python3

# from math import *
# from sklearn import tree
# import matplotlib.pyplot as plt
from GestorProblema import GestorProblema
from csvReader import csvReader
from LD.Problem import Problem

nameProblem = "Basic"
nameRestricciones = "Normal"

testType1 = "data/easy"
testType2 = "data/medium"
testType3 = "data/hard"
prob1 = Problem()
prob2 = Problem()
prob3 = Problem()
c = csvReader()

Alumnos = c.readstudents(testType1 + "/alumnos.csv")
Profesores = c.readprofessors(testType1 + "/profesores.csv")
Asignaturas = c.readsubjects(testType1 + "/asignaturas.csv")
Aulas = c.readaulas(testType1 + "/aulas.csv")

prob1.students = Alumnos
prob1.professors = Profesores
prob1.subjects = Asignaturas
prob1.rooms = Aulas

Alumnos = c.readstudents(testType2 + "/alumnos.csv")
Profesores = c.readprofessors(testType2 + "/profesores.csv")
Asignaturas = c.readsubjects(testType2 + "/asignaturas.csv")
Aulas = c.readaulas(testType2 + "/aulas.csv")

prob2.students = Alumnos
prob2.professors = Profesores
prob2.subjects = Asignaturas
prob2.rooms = Aulas

Alumnos = c.readstudents(testType3 + "/alumnos.csv")
Profesores = c.readprofessors(testType3 + "/profesores.csv")
Asignaturas = c.readsubjects(testType3 + "/asignaturas.csv")
Aulas = c.readaulas(testType3 + "/aulas.csv")
Restricciones = c.readrestricciones(testType1 + "/restricciones.csv")

prob3.students = Alumnos
prob3.professors = Profesores
prob3.subjects = Asignaturas
prob3.rooms = Aulas

GestorProblema.optimize(prob1, Restricciones)
GestorProblema.optimize(prob3, Restricciones)
GestorProblema.optimize(prob2, Restricciones)

prob1.result.print_result()
prob2.result.print_result()
prob3.result.print_result()
