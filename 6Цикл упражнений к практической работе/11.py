__author__ = 'Evgeny'
def fun(n, k):
    posl = [1 for i in range(k)]
    for i in range(n-k+1):
        summa = sum(posl)
        for j in range(k-1):
            posl[j] = posl[j+1]
        posl[k-1] = summa
    return posl[k-1]
inp = list(map(int, input().split()))
k = inp[0]
n = inp[1]
if 0 <= n <= k-1:
    print(1)
else:
    print(fun(n, k))