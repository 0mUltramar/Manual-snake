# Использовать функции из задач 1, 2 для решения задания 2 из урока 2:
# Программа, которая считывает два числа и выводит их сумму


def catchDigitsFromUser():
    ''' функция для получения 2 значений от пользователя '''
    a = float(input('Введите первое число:'))
    b = float(input('Введите второе число:'))
    return a, b


def sumTwoDigits(a, b):
    return a + b


def pazzle():
    a, b = catchDigitsFromUser()
    total = sumTwoDigits(a, b)
    return total


result = pazzle()

try:
    print("Сумма чисел равна:", result)
except ValueError:
    print('Какая-то херня, а не цифры')
