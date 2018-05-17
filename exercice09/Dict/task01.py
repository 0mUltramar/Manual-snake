# Создать словарь из слов, которые введёт пользователь. Ключи - слова, значения - их порядок расположения в исходном тексте.
# Например, текст *я понял, что эти так быстро проходят*. Словарь получится:
# ```python
# a = {'я': 1, 'понял,': 2, 'что': 3, 'эти': 4, 'так': 5, 'быстро': 6, 'проходят': 7}

inputStr = input("Введите текст: ")


def worlds_count(s: str) -> int:
    """ подсчитываем количество элементов в списке \
    если в строке пусто, то 0, иначе считаем пробелы. \
    Если строка заканчивается пробелом, то каунтер посчитает верно \
    инча нужно прибавить +1, т.к. в конце нет пробела и 1 слово будет пропущенно """
    if not s:
        return 0
    count = s.count(' ')
    if not s.endswith(' '):
        count += 1
    return count


# формируем список из строки
list_worlds = inputStr.split(" ")

# формируем список индексов для списка слов
list_index = [i for i in range(worlds_count(inputStr))]


def make_dictionary(list_a: list, list_b: list) -> dict:
    dictionaryFromString = dict(zip(list_a, list_b))
    return dictionaryFromString


print("готово! Ваш словарь готов, сэр!: {}".format(make_dictionary(list_worlds, list_index)))
