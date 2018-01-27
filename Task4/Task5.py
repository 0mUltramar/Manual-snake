print("Посчитаем количество четных числел в введеном числе")

x = input("Введите натуральнео число: ")

try:

    evenNumb = 0

    if int(x) > 0:
        # Формируем кортеж из х
        for i in tuple(x):
            # Собираем и подсчитываем значения, которые деляться на 2 без остатка
            if int(i) % 2 == 0:
                evenNumb += 1
        print("Количество четных цифр в числе: {}".format(evenNumb))

    elif int(x) == 0:
        print("Ноль не является натуральным числом. Введи другое число")

    else:
        print("Отрицательное число не является натуральным!!!")

except ValueError:
    print("Не пытайся")

except SyntaxError:
    print("Да что ты там куришь")

except UnicodeDecodeError:
    print('Шта?')

