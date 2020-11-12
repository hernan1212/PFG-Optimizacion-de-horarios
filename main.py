#!/usr/bin/python3

# from math import *
# from sklearn import tree
# import matplotlib.pyplot as plt
from LD.tipoRest import varP
from GestorProblema import GestorProblema as gp
from csvReader import csvReader
from LD.Problem import Problem

nameProblem = "Intento 1"
nameAlgorithm = "Basic"
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

gp.optimize(prob, Restricciones)

# prob.states.print_result()

