
# Выведу количество часов и минут без палева и таможенных сборов

setMinutes = int(input("Введите количество минут: "))
showHours = setMinutes // 60 % 24 # // - целочисл. деление, возвращаем только целую часть деления
showMinutes = setMinutes % 60 # % - возвращает остаток
# подробнее можно узнать на http://pythonicway.com/python-operators

print("На часах: {0:02d}:{1:02d}".format(showHours, showMinutes))
