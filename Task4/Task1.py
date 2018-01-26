print("выведу числа от 1 до 5 тремя способами")
a = 1
print("способ 1")
while 0 < a <= 5:
    print(a, '', end='')
    a += 1
print()
print()

print("способ 2")
for i in [1, 2, 3, 4, 5]:
    print(i, '', end='')
print()
print()

print("способ 3")

for i in range(1, 6):
    print(i, '', end='')
print()
