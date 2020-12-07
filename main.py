#!/usr/bin/python3
# from math import *
# from sklearn import tree
# import matplotlib.pyplot as plt
from GestorProblema import GestorProblema
from csvReader import csvReader
from LD.Problem import Problem
import sys
import argparse
import time

nameProblem = "Algoritmo de optimizacion de planificacion de recursos."
nameAlgoritmo = "Algoritmo genetico"
possibilities = ["easy", "medium", "hard", "very_hard", "exec"]
logs = True

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--information", help="Mostrar información del programa", action="store_true")
parser.add_argument("-q", "--quiet", help="No mostrar logs", action="store_true")
parser.add_argument("-f", "--file", help="Grupo de ficheros a procesar: easy, medium, hard o exec")
args = parser.parse_args()

if args.information:
    print("Nombre del problema: " + nameProblem)
    print("Algoritmo utilizado: " + nameAlgoritmo)

if args.file and args.file in possibilities:
    testType = "data/" + args.file
else:
    print("No se ha introducido un nombre de archivo.")
    print("Los nombres permitidos son:   easy    medium  hard   very_hard   exec")
    sys.exit()

if args.quiet:
    logs = False

prob = Problem()
c = csvReader(logs)
start_time = time.time()

Alumnos = c.readstudents(testType + "/alumnos.csv")
Profesores = c.readprofessors(testType + "/profesores.csv")
Asignaturas = c.readsubjects(testType + "/asignaturas.csv")
Aulas = c.readaulas(testType + "/aulas.csv")
Restricciones = c.readrestricciones(testType + "/restricciones.csv")

prob.students = Alumnos
prob.professors = Profesores
prob.subjects = Asignaturas
prob.rooms = Aulas

GestorProblema.optimize(prob, Restricciones, logs)

prob.result.print_result()

print("El tiempo de ejecución ha sido: " + str(time.time() - start_time))
