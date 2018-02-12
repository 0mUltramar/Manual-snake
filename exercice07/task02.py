def get_digital():
    x = float(input('Введите первое число:'))
    y = float(input('Введите второе число:'))
    return x, y


try:
    print("Вы указали числа", get_digital())
except ValueError:
    print('Какая-то херня, а не цифры')
