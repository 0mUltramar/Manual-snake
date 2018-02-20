# Использовать функции из задач 1, 2 для решения задания 2 из урока 2:
# Программа, которая считывает два числа и выводит их сумму


def catch_digits_from_user():
    try:
        ''' функция для получения 2 значений от пользователя '''
        a = float(input('Введите первое число:'))
        b = float(input('Введите второе число:'))
        return a, b
    except ValueError:
        print('Какая-то херня, а не цифры')
        exit()


def sum_two_digits(a, b):
    """ Функция сложения двух аргументов"""
    return a + b


def assemble_func_pazzle():
    """Из функции catch_digits_from_user()  получает 2 значения, введенных
    пользователем с клавиатуры. Далее, вычисляем сумму этих значений
    в функции sum_two_digits() """
    a, b = catch_digits_from_user()
    total = sum_two_digits(a, b)
    return total


print("Сумма чисел равна:", assemble_func_pazzle())

