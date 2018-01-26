x = (input("Введите положительное целое число:"))
try:
    x = int(x)
    if int(x) != abs(x):
        print("Вы ввели отрицательное число. Не накаляй, введи положительное!")
    else:
        if float(x) != int(x):
            print("Ты заставляешь меня снова на тебя орать. ВВЕДИ ЦЕЛОЕ ЧИСЛО!")
        else:
            #формируем список
            theSum = 0
            for i in range(1, x):
                theSum += i
            print("Сумма чисел от 1 до {0} = {1}".format(x, theSum))
except ValueError:
    print("Какая-то херня, браток")
except Exception:
    print("Даже я не оиждал такой ереси")
# язык Python за десять минут
