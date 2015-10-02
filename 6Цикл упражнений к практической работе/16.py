__author__ = 'Evgeny'
N = int(input())
if N == 0:
    print(1)
elif N == 1:
    print(1)
    print(1, 1)
else:
    print(1)
    print(1, 1)
    a = [1, 1]
    for i in range(N-1):
        for j in range(len(a)-1):
            a.insert(2*j+1, a[2*j+1]+a[2*j])
        for j in range((len(a)-3)//2):
            a.pop(2+j)
        print(' '.join(map(str, a)))