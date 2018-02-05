'''Заполнить список из шести элементов произвольными целочисленными значениями.
Вывести список на экран в обратной последовательности.
Два варианта получения обратной последовательности: с приминением цикла и без него.'''

# подключаем модель с функциями для генерации случайных чисел и назначаем короткий алиас
import random as rnd

print("Создаю список с 6 целочисленными значениями и выведу н аэкран в обратном порядке")
# Указываем ограничение в списке
listLim = 6

# rnd.randint(A, B) - генерит случайное целое число N, где A ≤ N ≤ B, упаковываем в квадр. скобки,
# тем самым заюзаем конструктор списков
i = [rnd.randint(1, 100) for _ in range(listLim)]
print("Вот что нагенерили: {}".format(i))
list.reverse(i)
print("Тот же список, только в профиль: {}".format(i))

# второй способ
print("~" * 50)
revList = []
for i in range(7):
    a = [rnd.randint(100, 1000)]
    revList.append(a)
print("Список в естественной последовательности: {}".format(revList))
list.reverse(revList)
print("Список в обратном порядке: {} ".format(revList))