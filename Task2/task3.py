# Программа вычисляет гипотенузу по двум катетам

hiMessage = ("Без регистрации и смс получи гипотензу прям. треуг. просто введя катеты a и b.")
print(hiMessage)
count = 0
a = input('катет a: ')
b = input('катет b: ')
gipotenuza = math.sqrt(a ** 2 + b ** 2)
print("Гиотенуза: %.2f" % gipotenuza)
