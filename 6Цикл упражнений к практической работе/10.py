A = list(map(int, input().split()))
t = int(input())
N = len(A)
for i in range (t):
    A.insert(N-1-A[N-1], A[N-1])
    A.pop()
print(' '.join(map(str, A)))