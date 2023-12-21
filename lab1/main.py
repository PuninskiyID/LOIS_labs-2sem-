##############################
# Лабораторная работа №1 по дисциплине ЛОИС
# Выполнена студентами группы 121702 БГУИР Пунинский И.Д , Целиков Ф.В.
# Вариант 4: выполнить импликацию методом Вебера
# Файл содержит реализацию системы прямого нечётеого логического вывода
##############################

import sys
import time
import re
from parser import *
from logic import *
import warnings


[fuzzy_sets, rules] = readFile("data.txt")
numOfAddableSet = 0
doneInferenceArr = []


def find_fuzzy_sets_for_rule(fuzzy_sets, rule):
	fuzzy_set_1 = FuzzySet("", [])
	fuzzy_set_2 = FuzzySet("", [])
	for fuzzy_set in fuzzy_sets:
		if fuzzy_set.name == rule[0]:
			fuzzy_set_1 = fuzzy_set
			break
	for fuzzy_set in fuzzy_sets:
		if fuzzy_set.name == rule[1]:
			fuzzy_set_2 = fuzzy_set
			break

	return fuzzy_set_1, fuzzy_set_2

def check_premise_usability(premise, predicateA):
	if premise.my_list[0][0] == predicateA.my_list[0][0]:
		if premise.name == predicateA.name:
			return False
		else:
			return True
	else:
		return False

numOfAddableSet = 0
usedRules = []

def data_output(predicateA, predicateB, premise):
	print("\n" + '-' * 50)
	print('Predicate_1: ' + predicateA.name + str(predicateA.my_list))
	print("Predicate_2: " + predicateB.name + str(predicateB.my_list))
	print("Premise: " + premise.name + str(premise.my_list))

def premise_cycle(fuzzy_sets, rules, anyOutput):
	used_Rules = []
	for premise in fuzzy_sets:
		if premise not in doneInferenceArr:
			new_premise = []
			[used_Rules, anyOutput, new_premises] = rule_cycle(rules, used_Rules, premise, anyOutput)			
			for p in new_premises:
				fuzzy_sets.append(p)
			doneInferenceArr.append(premise)	
	anyOutput = 0
	return anyOutput, fuzzy_sets, rules

def rule_cycle(rules, usedRules, premise, anyOutput):
	new_premises = []
	for rule in rules:
		if rule not in usedRules:
			[predicateA,predicateB] = find_fuzzy_sets_for_rule(fuzzy_sets, rule)  
			if check_premise_usability(premise, predicateA):
				usedRules.append(rule)
				anyOutput = 1
				data_output(predicateA, predicateB, premise)
				global numOfAddableSet
				new_premises.append(solution(predicateA, predicateB, premise, 'Y' + str(numOfAddableSet)))
				numOfAddableSet = numOfAddableSet + 1
	return usedRules, anyOutput, new_premises


anyOutput = 1
while anyOutput == 1:
	[anyOutput, fuzzy_sets, rules] = premise_cycle(fuzzy_sets, rules, anyOutput)






