A = '1 2 3 4 5'.split()
A.insert(0, A[len(A)-1])
A.pop()
print(' '.join(A))