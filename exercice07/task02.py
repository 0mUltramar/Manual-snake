# функция для ввода чисел

def get_digital():
    a = float(input('Введите первое число:'))
    b = float(input('Введите второе число:'))
    return a, b


try:
    print("Вы указали числа", get_digital())
except ValueError:
    print('Какая-то херня, а не цифры')
