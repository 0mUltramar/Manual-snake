#Дано натуральное число n. Выведите все числа от 1 до n. Без использования циклов.

input_n = input("введите натуральное число: ")


def check_input(a):
    try:
        if int(a) is True and a > 0:
            pass
        else:
            print("число отрицательное")
    except (NameError, TypeError):
        print("вы ввели не натуральное число")

input_n = int(input_n)
check_input(input_n)

print(*range(input_n))