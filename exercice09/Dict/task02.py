# Дан список чисел, который может содержать до 100000 чисел (каждое число от 0 до 1000). \
# Определите, сколько в нем встречается различных чисел.
# Эту задачу на Питоне можно решить в одну строчку, но нам нужно с помощью словаря.

import random as rnd

lst = [rnd.randint(0, 10) for i in range(100)]

print(lst)

a = {}

for value in lst:
    try:
        count = a[value]
    except KeyError:
        a[value] = 1
        continue
    a[value] += 1
print(a)

