# Проверить, что хотя бы одно из чисел a или b оканчивается на 0
print("Проверю на то, что хотя бы одно из чисел таки заканчивается на ноль")

a = int(input("введите число а: "))
b = int(input("введите число b: "))

# пробежимся по условиям. Оба числа могу заканчиваться на ноль, вообще не заканчиваться на ноль,
# любое из двух может заканчиваться на ноль

# проверяем на остаток
if a % 10 == 0:

    if b % 10 == 0:
        print("a = {} и b = {} сидели на трубе, оба заканчивались на ноль".format(a, b))

    elif b % 10 != 0:
        print("только a = {} заканчивается на ноль!".format(a))

elif b % 10 == 0:

    if a % 10 != 0:
        print("только b = {} заканчивается на ноль!".format(b))
else:
    print("ни одно из введенных чисел не заканчивается на ноль")
