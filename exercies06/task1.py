import random
'''Заполнить список из шести элементов произвольными целочисленными значениями. Вывести список на экран'''

# http://ps.readthedocs.io/ru/latest/random.html Python 3: Генерация случайных чисел (модуль random)

print('Генерация случайных чисел слишком важна, чтобы оставлять её на волю случая')

# для создания списка используем конструктор списков — list comprehension — цикл внутри квадратных скобок
makeRandomInt = [random.randint(10, 100) for x in range(7)]

print("Вот ваш список 6 рандомных значений {}".format(makeRandomInt))
