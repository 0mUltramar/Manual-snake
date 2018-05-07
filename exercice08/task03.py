"Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя их пробелами или новыми \
строками. При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется)."

from . import task02



def print_n_reverese(n):
    """Выводит на экран все цифры числа по одной в обратном порядке"""
    if n // 10 > 0:
        print(n % 10)
        print_n_reverese(n // 10)
    else:
        print(n)
        exit()

N = input("Введите натруральное число: ")

# Вызываем функцию проверки числа на целое положительное из задания 2
task02.check_input(N)


print_n_reverese(N)