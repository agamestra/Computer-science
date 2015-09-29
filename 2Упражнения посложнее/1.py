A = '1 2 3 4 5'.split()
for i in range (len(A)//2):
    A[2*i], A[2*i+1] = A[2*i+1], A[2*i]
print(' '.join(A))