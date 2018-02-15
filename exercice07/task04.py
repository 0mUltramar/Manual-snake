# Написать функцию, принимающую длину стороны квадрата и рассчитывающую периметр квадрата, его площадь и диагональ.
# Сделать два и более варианта функции, которые должна отличаться количеством возвращаемых переменных. Не забыть про
# проверки входных данных в самой функции.


def inpSideLenght():
    a = float(input("Введите длину стороны квардрата: "))
    return a


def calcPerimeter(a):
    p = a * 4
    return p


def calcArea(a):
    s = a ** 2
    return s

def calcDiagonal(a):
    b = (a ** 2 * 2) ** 0.5
    return b

def calcSquare():
    inpSideLenght()
    calcPerimeter()
    calcArea()
    calcDiagonal()
    return