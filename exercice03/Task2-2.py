# Настоящее задание №2 находится тут. Спасибо, что делаешь код ревью)

print('Программа вычислит четверть, в которой лежит точка на графике')
X = float(input("Введите число, соотвествующее оси Х: "))
Y = float(input("Введите число, соотвествующее оси Y: "))

try:
    if X == 0:

        if Y != 0:
            print ('OX')

        elif Y == 0:
            print('BINGO! Black ZERO!')

    elif Y == 0:
        if X != 0:
            print('OY')

    elif X > 0 and Y > 0:
        print('I')

    elif X < 0 and Y < 0:
        print('III')

    elif X < 0 and Y > 0:
        print('II')

    else:
        print('IV')

except():
    print('Вероятно, вы ввели не число, попробуйте еще раз!')