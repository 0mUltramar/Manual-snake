# Дан текст:
#
# Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non,
# je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier
# toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus,
# vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites
# Выведите все слова, встречающиеся в
# тексте, по одному на каждую строку.
#
# Слова должны быть отсортированы по убыванию их частоты появления в тексте, а при одинаковой частоте появления — в
# лексикографическом порядке.
#
# Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости
# слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота
# встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет
#  сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму.
# Это почти то, что требуется в задаче.
import re

someStr = string = "Eh bien, mon prince. Gênes et Lucques ne sont plus que des apanages, des поместья, de la famille Buonaparte. Non, je vous préviens que si vous ne me dites pas que nous avons la guerre, si vous vous permettez encore de pallier toutes les infamies, toutes les atrocités de cet Antichrist (ma parole, j'y crois) — je ne vous connais plus, vous n'êtes plus mon ami, vous n'êtes plus мой верный раб, comme vous dites"

# очищаем от левых символов строку
someStr = re.sub(r"['.,()—]", "", someStr)

# преобразуем строку в список
lst = someStr.split(" ")

dictFromList = {}

for value in lst:
    try:
        count = dictFromList[value]
    except KeyError:
        dictFromList[value] = 1
        continue
    dictFromList[value] += 1


sortList = [(item[1], item[0]) for item in dictFromList.items()]
sortList.sort()
sortList.reverse()


sortDic = {}
for item in sortList:
        word_count = item[0]
        word = item[1]
        if word_count not in sortDic:
            sortDic[word_count] = [word]
        else:
            sortDic[word_count].append(word)

print(sortList)
print(sortDic)
for key, words in sortList:
    print(words)