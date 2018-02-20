# Написать функцию, приминмающую номер месяца и возвращающую время года, которому принадледжит месяц. Не забыть про
# проверки входных данных в самой функции. Вызвать функцию в цикле несколько раз для случайных значений номера месяца.

import re

monthShortNumbersList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
monthFullNumbersList = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
monthShortNamesListEn = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
monthFullNamesListEn = ["January", "February", "March", "April", "May", "June", "July", "August",
                        "September", "October", "November", "December"]
monthShortNamesListRu = ["янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
monthFullNamesListRu = ["январь", "февраль", "март", "апрель", "май", "июнь",
                        "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

# Формируем общий список вариантов месяца
allMonthVar = monthShortNumbersList + monthFullNumbersList + monthShortNamesListRu \
              + monthShortNamesListEn + monthFullNamesListRu + monthFullNamesListEn
# приводим значения в списке к нижнему регистру
allMonthVar = [element.lower() for element in allMonthVar]


def input_month():
    """ получаем любое значение с клавиатуры и, если можем, привеодим его к нижн. регистру"""
    a = input("Введите мясяц: ")
    a = a.lower()
    return a


def find_month_index(a):
    if bool(re.match('^[0][1-9]$|^[1-9][0-2]$|[1-9]|^[a-z]]')) is True:
        allMonthVar.index(a)
    else:
        print("Я столько для тебя сделал, а ты таки умудрился ввести месяц в неизвестном формате")
        exit()

