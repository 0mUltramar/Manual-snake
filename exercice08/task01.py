# Создайте функции:
# *генерации двумерного массива случайных чисел с заданными размерами
# *поиска максимальных чисел в каждой строке двумерного массива(2 функции)
# *проверки любой переменной на то, что она содержит положительное целое число и приведение переменной к int

# Поместите полученные функции в отдельный модуль. Итоговую программу оформите в отдельном модуле(файле).
# Создайте двумерный массив 10х10 из случайных чисел.Ввод размера массива сделать с клавиатуры.
# Вычислить максимальный элемент в каждой строке массива и вывести полученный список на экран.
#
from . import functions

varInputLenght = input("Введите длину таблицы (целое положительное число): ")
varInputHeight = input("Введите высоту таблицы (целое положительное число): ")

functions.check_input(varInputLenght, varInputHeight)

print("Максимальные значения из каждой строки: {} ".format(
    functions.get_max_in_matrix(functions.generate_matrix(varInputLenght, varInputHeight))))