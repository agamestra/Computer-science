__author__ = 'Evgeny'
N = int(input())
a = list(map(int, input().split()))
number = 0
for i in range(N):
    for j in range(N):
        if a[i] > a[j]:
            number += 1
    if number == N//2:
        print(a[i])
        break
    else:
        number = 0