''' Заполнить список из десяти элементов произвольными целочисленными значениями.
Затем четные элементы расположить в начале списка, нечетные - в конце.'''

import random as rnd

# лист с общими значениями
communList = [rnd.randint(1, 1000) for x in range(10)]

# лист с четными значениями из общего листа
sssortList = []

for x in communList:
    if x % 2 == 0:
        sssortList.insert(0, x)
    else:
        sssortList.append(x)

print("Несортированный список: {}".format(communList))
print("Сортированный список:   {}".format(sssortList))
