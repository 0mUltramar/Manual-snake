# Создайте функции:
# *генерации двумерного массива случайных чисел с заданными размерами
# *поиска максимальных чисел в каждой строке двумерного массива(2 функции)
# *проверки любой переменной на то, что она содержит положительное целое число и приведение переменной к int


import random as rnd


def generate_matrix(x: int, y: int) -> list:
    matrix = list()
    for i in range(0, x):
        row = list()
        for j in range(0, y):
            row.append(rnd.randint(0, 100))
        matrix.append(row)
        print(row)
    return matrix


def get_max(row: list) -> int:
    max = 0
    for value in row:
        if value > max:
            max = value
    return max


def get_max_in_matrix(matrix: list) -> list:
    maxList = list()
    for row in matrix:
        maxList.append(get_max(row))
    return maxList


def check_input(a, b):
    """Приводим значения к int, если возможно, проверяем на положительное"""
    try:
        int(a)
        int(b)
        if a > 0:
            if b > 0:
                return int(a), int(b)
            else:
                print("Вы ввели высоту таблицы некорректно! Пошёл на хуй!")
        else:
            print("Вы ввели длинну таблицы некорректно! Пошёл на хуй!")
    except ValueError:
        print("Fuck u!")
