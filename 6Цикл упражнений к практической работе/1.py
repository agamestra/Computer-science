A = input().split()
for i in range(len(A)):
    print(A[((i+1)//2)*((-1)**i)], end=' ')

