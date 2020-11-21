#!/usr/bin/python3

# from math import *
# from sklearn import tree
# import matplotlib.pyplot as plt
from GestorProblema import GestorProblema
from csvReader import csvReader
from LD.Problem import Problem

nameProblem = "Basic"
nameRestricciones = "Normal"

prob = Problem()
c = csvReader()

Alumnos = c.readstudents("data/alumnos.csv")
Profesores = c.readprofessors("data/profesores.csv")
Asignaturas = c.readsubjects("data/asignaturas.csv")
Aulas = c.readaulas("data/aulas.csv")
Restricciones = c.readrestricciones("data/restricciones.csv")

prob.students = Alumnos
prob.professors = Profesores
prob.subjects = Asignaturas
prob.rooms = Aulas

GestorProblema.optimize(prob, Restricciones)

prob.result.print_result()
