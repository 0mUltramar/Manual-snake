# Написать функцию, приминмающую номер месяца и возвращающую время года, которому принадледжит месяц. Не забыть про
# проверки входных данных в самой функции. Вызвать функцию в цикле несколько раз для случайных значений номера месяца.

# Формируем словарь сезон-месяцы

seasons = {'Winter': ('1', '2', '12'),
           'Sping': ('3', '4', '5'),
           'Summer': ('6', '7', '8'),
           'Autumn': ('9', '10', '11')}

# формируем словарь для ассоциации между цифровым значением месяца и текстовым именем
months = {'1': ('01', '1', 'jan', 'january', 'янв', 'январь'),
          '2': ('02', '2', 'feb', 'february', 'фев', 'февраль'),
          '3': ('03', '3', 'mar', 'march', 'мар', 'март'),
          '4': ('04', '4', 'apr', 'april', 'апр', 'апрель'),
          '5': ('05', '5', 'may', 'may', 'май', 'май'),
          '6': ('06', '6', 'jun', 'june', 'июн', 'июнь'),
          '7': ('07', '7', 'jul', 'july', 'июл', 'июль'),
          '8': ('08', '8', 'aug', 'august', 'авг', 'август'),
          '9': ('09', '9', 'sep', 'september', 'сен', 'сентябрь'),
          '10': ('10', 'oct', 'october', 'окт', 'октябрь'),
          '11': ('11', 'nov', 'november', 'ноя', 'ноябрь'),
          '12': ('12', 'dec', 'december', 'дек', 'декабрь')}


def input_month():
    """ получаем любое значение с клавиатуры и, если можем, привеодим его к нижн. регистру"""
    a = input("Введите мясяц в формате 01 или 1 или полное/сокращенное название на русском или англ. яз.: ")
    a = a.lower()
    return a


def find_mont_in_set():
    """Проверяем, есть ли указанное позьзователем в функции input_month() значение в словаре months.
    Если есть, то выводим ключ, которому соотвествует введенное значение месяца."""
    monthval = input_month()
    for key in months.keys():
        if monthval in months[key]:
            return key


def find_season_by_month():
    """Получаем значение (номер) месяца из функции find_mont_in_set() и по нему получаем ключ,
    являющийся сезоном, к которому принадлежит месяц"""
    val = find_mont_in_set()
    for numb_of_month in seasons.keys():
        if val in seasons[numb_of_month]:
            return (numb_of_month)


print("Введенному месяцу соотвествует сезон: {}".format(find_season_by_month()))

# А теперь выполнение задания :)

import random as rnd


def find_season(m: "номер месяца от 1 до 12"):
    mInt = int(m)
    if 2 < mInt < 6:
        season = "Spring"
    elif 5 < mInt < 9:
        season = "Summer"
    elif 8 < mInt < 11:
        season = "Autumn"
    elif mInt == 12 or 0 < mInt < 3:
        season = "Winter"
    else:
        season = "Shit happens"

    return season


randomsDig = [rnd.randrange(1, 12, 1) for _ in range(1, 13)]

for i in randomsDig:
    print(i, find_season(i))
