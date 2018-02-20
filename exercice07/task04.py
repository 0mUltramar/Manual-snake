# Написать функцию, принимающую длину стороны квадрата и рассчитывающую периметр квадрата, его площадь и диагональ.
# Сделать два и более варианта функции, которые должна отличаться количеством возвращаемых переменных. Не забыть про
# проверки входных данных в самой функции.


def inp_side_lenght():
    """inp_side_lenght() позволяет пользователюё указать длину стороны квадрата. Проверяем введенное значение"""
    try:
        return float(input("Введите длину стороны квардрата: "))
    except ValueError:
        print("Вы ввели какую-то ересь. Введите число!")
        exit()


def calc_perimeter(a):
    """ calc_perimeter() считает периметр квадрата"""
    p = a * 4
    return p


def calc_area(a):
    """ calc_area() считает площадь квадрата"""
    s = a ** 2
    return s


def calc_diagonal(a):
    """ calc_diagonal() считает диагональ квадрата"""
    return (a ** 2 * 2) ** 0.5


def calc_square():
    """Объединяем функции для получения"""
    a = inp_side_lenght()
    p =calc_perimeter(a)
    ar = calc_area(a)
    di = calc_diagonal(a)
    return a, p, ar, di


a, p, ar, di = calc_square()


print("У квардрата с длинной стороны = {:.2f}:\nПериметр: {:.2f}\n"
      "Площадь: {:.2f}\nДиагональ:{:.2f}".format(a, p, ar, di))

print("Второй способ представления функции")


def square_calc():
    pirimeter = a * 4
    area = a ** 2
    diagonal = (area * 2) ** 0.5
    return pirimeter, area, diagonal


sides = inp_side_lenght()


per, ar, dia = square_calc()

print("У квардрата с длинной стороны = {:.2f}:\nПериметр: {:.2f}\n"
      "Площадь: {:.2f}\nДиагональ:{:.2f}".format(sides, per, ar, dia))