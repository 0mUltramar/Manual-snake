try:
    x = (input(':'))
    if x != abs(x):
        print("Вы ввели отрицательное число. Не накаляй, введи положительное!")
    else:
        if float(x) != int(x):
            print("Ты заставляешь меня снова на тебя орать. ВВЕДИ ЦЕЛОЕ ЧИСЛО!")
        else:
            print(x + 1)
except ValueError:
    print("Какая то хуйня")
except Exception:
    print("Даже я не оиждал такой ереси")
