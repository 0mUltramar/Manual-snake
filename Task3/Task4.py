# Дана следующая функция y = f(x):
# y = x + 1.5, при x > 10;
# y = 0, при x = 10;
# y = -x, при x < 10.

print("Программа вычисляет Y из функции y = f(x) по введенному значению X")
X = float(input('X = '))
if X > 10:
    Y = X + 1.5
    print("Y = {}".format(Y))
elif X == 10:
    Y = 0
    print("Y = {}".format(Y))
elif X < 10:
    Y = X * (-1)
    print("Y = {}".format(Y))

