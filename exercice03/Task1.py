# Вычислить модуль числа

# А вот более серьезная магия подъехала
print("Программа вычислит модуль числа")
setChislo = input("Введите число, чей модуль скрыт для вашего разума: ")
try:
    setChislo = float(setChislo)
    if setChislo < 0:
        print("Абракадабра!: \n", setChislo * (-1))

except():
    print('Введи число или не трать время!')

print('Абракадабра! Модуль числа {:.2f}'.format(setChislo))
