print('Сейчас для тебя найду произведение  чисел трехзначного числа, введенных с клавиатуры')

x = input('Введите трехзначное число: ')

try:
    xxx = 1
    # выполним ряд преобразований, чтобы можно было работать как с положительными, так и отриц. числами
    x = int(x)  # преобразуем в целое. Если не получится, попадем на except
    x = abs(x)  # далее будем использовать модуль числа
    x = str(x)  # преобразуем обратно в строку

    if 99 < int(x) < 999:
        for i in tuple(x):  # tuple()- формирует кортеж, вместо списка. Кортеж значительно быстрее списка.
            xxx = xxx * int(i)
        print('Произведение равно: {:d}'.format(xxx))

    else:
        print("только трехзначное число!!! А ты что ввел? Ты ввел {}! Смекаешь?".format(x))

except ValueError:
    print("Какая-то херня, а не трехзначное число")

except TypeError:
    print('Опять упоролся? Число должно быть ТРЕХЗНАЧНОЕ! ОДИНДВАТРИ!')

except UnicodeDecodeError:
    print('Шта?')
