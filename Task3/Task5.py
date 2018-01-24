print("Проверь, могут ли введеные три числа образовать треугольник и стать длинами его сторон.")

A = float(input("Введите первое число: "))
B = float(input("Введите второе число: "))
C = float(input("Введите третье число: "))


# Классическое неравенство треугольников для общих случаев: Сумма двух сторон должна быть больше третьей
triangleInequality = (A + B > C and A + C > B and B + C > A)

# Треугольник можно попытаться образовать только если его длины положительны (вообще нет, от дебрей отрицательной
# геометрии Лобачевского лучше воздержаться, чтобы не вызвать Сотону:)
generalCondition = (A > 0 and B > 0 and C > 0) and triangleInequality

# http://pco.iis.nsk.su/ICP/Introduction/dd3/node13.html


if generalCondition:



    if condition and A == B == C:
        print("Позравляю! Вы таки получили равносторонний треугольник")

