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


def sum_two_digits(a, b):
    return a + b


def assemble_func_pazzle():
    a, b = catch_digits_from_user()
    total = sum_two_digits(a, b)
    return total


result = assemble_func_pazzle()
print("Сумма чисел равна:", result)

