##############################
# Лабораторная работа №1 по дисциплине ЛОИС
# Выполнена студентами группы 121702 БГУИР Пунинский И.Д , Целиков Ф.В.
# Вариант 4: выполнить импликацию методом Вебера
# Файл содержит реализацию системы прямого нечётеого логического вывода
##############################

import sys
import time
import re
from source.parser import *
from source.logic import *
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)
timeout_seconds = 3  
start_time = time.time()

inferenceArr = []
doneInferenceArr = []

[parcels, rules] = readFile('data.txt')

for parcel in parcels:
    inferenceArr.append(parcel['list'])


while True:
    C = inferenceArr[0]
    if C not in doneInferenceArr:
        for rule in rules:
            predicateA = [item for sublist in [item['list'] for item in parcels if item['name'] == rule[0]] for item in sublist]
            predicateB = [item for sublist in [item['list'] for item in parcels if item['name'] == rule[1]] for item in sublist]
            wrongC = False
            for j, value in enumerate(predicateA):
                if len(predicateA) == len(C):
                    if predicateA[j][0] != C[j][0]:
                        wrongC = True
                else:
                    wrongC = True
            if not wrongC:
                print("\n" + str(rule[0]) + " = " + "{" + ", ".join([f"<{item[0]}, {item[1]}>" for item in predicateA]) + "}")
                print(str(rule[1]) + " = " + "{" + ", ".join([f"<{item[0]}, {item[1]}>" for item in predicateB]) + "}")
                print("Parcel = " + "{" + ", ".join([f"<{item[0]}, {item[1]}>" for item in C]) + "}")
                solution(predicateA, predicateB, C, inferenceArr)
                print("\n" + '-' * 50)
                

            inferenceArr = [value for value in inferenceArr if value != C]
            doneInferenceArr.append(C)

    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > timeout_seconds:
        break