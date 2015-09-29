A = '1 2 3 2 3 3'.split()
maxn = 0
n = 0
for i in range(len(A)):
    if A.count(A[i]) > maxn:
        maxn = A.count(A[i])
        n = A[i]
print(A[i])