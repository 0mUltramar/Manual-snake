print('hello!')
# подключаем модель с функциями для генерации случайных чисел и назначаем короткий алиас
import random as rnd

print("Создаю список с 6 целочисленными значениями и выведу на экран в обратном порядке")
# Указываем ограничение в списке
listLim = 6

print("Способ №1")

# rnd.randint(A, B) - генерит случайное целое число N, где A ≤ N ≤ B, упаковываем в квадр. скобки,
# тем самым заюзаем конструктор списков
iList = [rnd.randint(1, 100) for _ in range(listLim)]
findMax = max(iList)
print("Сгенерили список: {}".format(iList))
print("Самое большое число в списке: {}".format(findMax))  # значение функции max прозрачно жеж)
print("Индекс макс. позиции: ", iList.index(findMax))

# второй способ
print("~" * 50)
print("Способ №2")
# получаем максимальное значение
maxValue = 0
findPos = 0
for i in iList:
    if i > maxValue:
        maxValue = i
        findPos = iList.index(i)

# Получаем его индекс

print("Сгенерили список: {},\nполучили самое большое число в списке: {},\nИндекс найденного числа: {}".format(iList, maxValue, findPos))

# третий способ
print("~" * 50)
print("Способ №3, с другим способ получения списка")

"Генерим новый список"
revList = []
for i in range(listLim):
    a = rnd.randint(100, 1000)
    revList.append(a)
print("Список в естественной последовательности: {}".format(revList))
revList.sort(reverse=True) # Сортируем готовый список в от большего к меньшему
print("Самое большое число в списке: {} ".format(revList.pop(0))) # revList.pop(0) - выводим первую позицию на индексе 0
print("Индекс (внезапно): 0")