__author__ = 'Evgeny'
N = int(input())
a = list(map(int, input().split()))
k = int(input())
if N == k:
    print(sum(a))
else:
    lis = [0 for i in range(k)]
    max = sum(lis)
    for i in range(N-k):
        for j in range(k):
            lis[j] = a[j+i+1]
        if sum(lis) > max:
            max = sum(lis)
    print(max)