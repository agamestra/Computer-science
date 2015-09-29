input = open('/home/student/PycharmProjects/untitled/4Генерация случайных чисел/float_data.txt', 'r')
summa = 0
sumkvad = 0
n = 0
for i in range(int(150)):
    a = input.readline()
    summa += float(a)
    sumkvad += float(a)**2
    n += 1
print(summa)
print(sumkvad)
print(n)
print()
print(summa/n)
print(((sumkvad/n)-(summa/n)**2)**0.5)