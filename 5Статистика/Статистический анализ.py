input = open('/home/student/PycharmProjects/untitled/4Генерация случайных чисел/int_data.txt', 'r')
A = [0 for i in range(101)]
for i in range(int(1e6)):
    a = int(input.readline())
    A[a] += 1
print(A)
#for i in range(100):
#    print(str(i)+':'+A[i], end='', sep=' ')
print(A.index(max(A)))
print(A.index(min(A)))
print(101)