print("Заполню список из четырёх элементов введёными строковыми значениями и выведу полученный список на экран.     Изи")

mylist = []  # используем список, т.к. кортеж нельзя модифицировать
for i in range(4):
    a = input(str('Введи что нибудь: '))
    mylist.append(a)
print(mylist)