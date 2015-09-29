A = '1 2 2 3 3 3'.split()
for i in range(len(A)):
    if A.count(A[i]) == 1:
        print(A[i])