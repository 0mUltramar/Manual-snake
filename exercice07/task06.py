# Работаем с чужим кодом. В коде из файла https://github.com/groall/python_learning/blob/master/lesson_04_cycles
# /task03.py нужно заменить повторяющееся с циклах действие суммирования на вызов функции, функция должна работать с
# глобальной переменной sumNumbers

x = input('Введите целое положительное число: ')

if not x.isdigit():
    print("Вы ввели не число")
    exit()

xInt = int(x)
if xInt < 1:
    print("Число не положительное")
    exit()


def sum_numbers(endRange):
    """ Функция суммирует значения от 1 до переданного """
    global sumNumbers
    for i in range(1, endRange):
        sumNumbers += i
    return sumNumbers


sumNumbers = 0
sum_numbers(xInt)


print("Сумма", sumNumbers)

sumNumbers = 0
sum_numbers(xInt)


print("Сумма", sumNumbers)