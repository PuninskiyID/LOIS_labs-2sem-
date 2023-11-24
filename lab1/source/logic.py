##############################
# Лабораторная работа №1 по дисциплине ЛОИС
# Выполнена студентами группы 121702 БГУИР Пунинский И.Д , Целиков Ф.В.
# Вариант 4: выполнить импликацию методом Вебера
# Файл библиотека, реализующий прямой нечёткий вывод по Веберу
##############################
import numpy as np
import warnings


#Вычисление по Веберу

def countTNormRes(x, y):
    tValues = np.linspace(-np.inf, np.inf, 1000)
    tValues = np.where(tValues > 0, tValues, np.nan)
    fValues = x * np.exp(tValues * np.log(y)) + y * np.exp(tValues * np.log(x))
    limResult = np.max(fValues)
    if limResult < 1:
        return limResult
    else:
        return 1.0


def countRes(x, y):
    if x == 1.0:
        return y
    else:
        return 1.0

def findPredicate(A, B):
    predicate = []

    for i in A:
        line = []
        for j in B:
            pair = []
            res = countRes(i[1], j[1]) 
            pair.append("<{}, {}>".format(i[0], j[0]))
            pair.append(res)
            line.append(pair)

        predicate.append(line)

    return predicate

def findResultMatrix(matrix, C):
    resMatrix = []
    matrixC = [i[1] for i in C]

    for i in range(len(matrixC)):
        line = [countTNormRes(matrixC[i], x) for x in matrix[i]]
        resMatrix.append(line)

    return resMatrix

def findInference(multMatrix, B):
    inference = []

    for i in range(len(B)):
        column = []
        for j in range(len(multMatrix)):
            column.append(multMatrix[j][i])

        inference.append([B[i][0], findMaxElement(column)])

    return inference

def findMatrix(A, B, predicate):
    matrix = []

    for i in range(len(A)):
        line = []
        for j in range(len(B)):
            line.append(predicate[i][j][1])
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

def solution(A, B, C, inferenceArr):
    predicate = findPredicate(A, B)
    print("\nPredicate:")
    for i in predicate:
        print(", ".join([f"<{item[0]}, {item[1]}>" for item in i]))

    matrix = findMatrix(A, B, predicate)
    printList("Matrix", matrix)

    resMatrix = findResultMatrix(matrix, C)
    printList("Result matrix", resMatrix)

    inference = findInference(resMatrix, B)

    inferenceArr.append(inference)

    print("\nInference:")
    print("{" + ", ".join([f"<{item[0]}, {item[1]}>" for item in inference]) + "}")