# Я посчитаю нужное количество парт для ваших классов исходя из количества учеников.
# Внимание, я могу посчитать не более чем для трех классов за раз.
from math import ceil,fsum

print("Введите кол-во учащихся в каждом классе")

pupilsInClass1 = int(input("Учеников в классе А :"))
pupilsInClass2 = int(input("Учеников в классе Б :"))
pupilsInClass3 = int(input("Учеников в классе В :"))

needDesks1 = ceil(pupilsInClass1 / 2)
needDesks2 = ceil(pupilsInClass2 / 2)
needDesks3 = ceil(pupilsInClass3 / 2)
AgregateDesks = sum([needDesks1,needDesks2,needDesks3])
print("Требуется парт для классов: А- {0}, Б- {1}, В- {2}".format(needDesks1, needDesks2, needDesks3))
print("Всего парт требуется: ",AgregateDesks)