# Заполнить список из десяти элементов произвольными целочисленными значениями (без использования цикла).
# Удалить те элементы, значения которых не кратны 3.

import random as rnd

limitList = 10

tenList = [rnd.randint(1, 1000) for i in range(limitList)]
iList = [x for x in tenList if x % 3 == 0]

print("Исходный список из 10 значений: {}".format(tenList))
print("Список из значений, кратных трем: {}".format(iList))
