__author__ = 'Evgeny'
lis = []
N = int(input())
for i in range(N):
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    if b > len(lis)-1:
        for j in range(b-len(lis)+1):
            lis.append(0)
    for j in range(b-a+1):
        lis[a+j] += 1
print(lis[int(input())])