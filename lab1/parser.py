##############################
# Лабораторная работа №1 по дисциплине ЛОИС
# Выполнена студентами группы 121702 БГУИР Пунинский И.Д , Целиков Ф.В.
# Вариант 4: выполнить импликацию методом Вебера
# Файл библиотека, реализующий парсинг файла для последующей обработки
##############################
import re


def parseRule(rule: str):
    pattern = r'^([A-Z]\d*)~>([A-Z]\d*)$'
    match = re.match(pattern, rule)

    if match:
        return [match.group(1), match.group(2)]

    return None

def parsePremise(premise: str):
    generalPattern = r'^[A-Z][0-9]*=\{<([a-z]+\d*),(1\.0|0\.\d+)>((,<([a-z]+\d*),(1\.0|0\.\d+)>)*)\}$'

    if not bool(re.match(generalPattern, premise)):
        return None

    groupPattern = r'^([A-Z0-9]+)=\{(.+?)\}$'
    match = re.match(groupPattern, premise)

    if match:
        name = match.group(1)
        pairs = re.findall(r'<([a-z]+\d*),(1\.0|0\.\d+)>', match.group(2))

        nameSet = set()
        premiseList = []
        for pair in pairs:
            pairName = pair[0]
            if pairName in nameSet:
                return None
            else:
                nameSet.add(pairName)
                premiseList.append([str(pairName), float(pair[1])])

        return {'name': name, 'list': premiseList}

    return None

def readFile(filePath: str):
    premises = []
    rules = []
    with open(filePath, 'r') as file:
        for line in file: 
            line = line.replace(" ", "").strip()
            item = parsePremise(line)
            if item is not None:
                premises.append(item)
            else:
                item = parseRule(line)
                if item is not None:
                    rules.append(item)
    return get_fuzzy_sets(premises), rules

class FuzzySet:
    def __init__(self, name, my_list):
        self.name = name
        self.my_list = my_list

    def display_info(self):
        print(f"Name: {self.name}")
        print("List:")
        for item in self.my_list:
            print(f"  {item[0]}: {item[1]}")

def parse_to_fuzzy_set(data):
    instances = []
    for entry in data:
        name = entry['name']
        my_list = entry['list']
        instance = FuzzySet(name, my_list)
        instances.append(instance)
    return instances


def get_fuzzy_sets(data):
    set_of_fuzzy_sets = parse_to_fuzzy_set(data)
    return set_of_fuzzy_sets