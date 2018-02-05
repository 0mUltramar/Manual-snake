print('hello!')
# подключаем модель с функциями для генерации случайных чисел и назначаем короткий алиас
import random as rnd

print("Создаю список с 6 целочисленными значениями и выведу на экран в обратном порядке")
# Указываем ограничение в списке
listLim = 6

# rnd.randint(A, B) - генерит случайное целое число N, где A ≤ N ≤ B, упаковываем в квадр. скобки,
# тем самым заюзаем конструктор списков
iList = [rnd.randint(1, 100) for _ in range(listLim)]
print("Сгенерили список: {}".format(iList))
print("Самое большое число в списке: {}".format(max(iList)))  # значение функции max прозрачно жеж)

# второй способ
maxValue = 0
for i in iList:
    if i > maxValue:
        maxValue = i
print('Самое большое число в списке: {}'.format(maxValue))

# третий способ

print("~" * 50)

revList = []
for i in range(listLim):
    a = rnd.randint(100, 1000)
    revList.append(a)
print("Список в естественной последовательности: {}".format(revList))
revList.sort(reverse=True)
print("Самое большое число в списке: {} ".format(revList.pop(0)))