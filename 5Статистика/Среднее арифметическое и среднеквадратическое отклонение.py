input = open('/home/student/PycharmProjects/untitled/4Генерация случайных чисел/float_data.txt', 'r')
summa = 0
sumkvad = 0
n = 0
nmax = -1
nmin = 101
imax = 0
imin = 0
for i in range(int(1e6)):
    a = float(input.readline())
    summa += a
    sumkvad += a**2
    n += 1
    if a > nmax:
        nmax = a
        imax = i
    if a < nmin:
        nmin = a
        imin = i
print(summa)
print(sumkvad)
print(n)
print()
print(summa/n)
print(((sumkvad/n)-(summa/n)**2)**0.5)
print()
print(nmax)
print(imax)
print()
print(nmin)
print(imin)