##############################
# Лабораторная работа №1 по дисциплине ЛОИС
# Выполнена студентами группы 121702 БГУИР Пунинский И.Д , Целиков Ф.В.
# Вариант 4: выполнить импликацию методом Вебера
# Файл библиотека, реализующий прямой нечёткий вывод по Веберу
##############################
import numpy as np
import warnings
from parser import *

def countTNormRes(x, y):
    if(y == 1):
        return x
    elif(x == 1):
        return y
    else:
        return 0.0

def countRes(x, y):
    if x == 1.0:
        return y
    else:
        return 1.0

def findPredicate(A, B):
    variables = []
    for var_a in A.my_list:
        variable_line = [] 
        for var_b in B.my_list:
            variable = []
            variable.append(var_a[0])
            variable.append(var_b[0])
            variable.append(countRes(var_a[1], var_b[1]))
            variable_line.append(variable)
        variables.append(variable_line)
    return variables

def findResultMatrix(matrix, C):
    resMatrix = []
    matrixC = [i[1] for i in C.my_list]

    for i in range(len(matrixC)):
        line = [countTNormRes(matrixC[i], x) for x in matrix[i]]
        resMatrix.append(line)

    return resMatrix

def findInference(multMatrix, B):
    inference = []

    for i in range(len(B.my_list)):
        column = []
        for j in range(len(multMatrix)):
            column.append(multMatrix[j][i])
        inference.append([B.my_list[i][0], findMaxElement(column)])

    return inference

def findMatrix(predicate):
    matrix = []

    for i in range(len(predicate)):
        line = []
        for j in range(len(predicate[i])):
            line.append(predicate[i][j][len(predicate[i][j]) - 1])
        matrix.append(line)

    return matrix


def findMaxElement(column):
    maxEl = 0.0
    for i in column:
        if i > maxEl:
            maxEl = i

    return maxEl

def printList(name, lst):
    print("\n " + name + ":")
    for i in lst:
        print(i)

def solution(A, B, C, name_for_new_predicate):
    predicate = findPredicate(A, B)
    for i in predicate:
        print(i)

    matrix = findMatrix(predicate)
    #printList("Matrix", matrix)

    resMatrix = findResultMatrix(matrix, C)
    #printList("Result matrix", resMatrix)

    inference = findInference(resMatrix, B)

    print("\nInference:")
    print("{" + ", ".join([f"<{item[0]}, {item[1]}>" for item in inference]) + "}")

    predicateToAdd = FuzzySet(name_for_new_predicate, inference)

    return predicateToAdd