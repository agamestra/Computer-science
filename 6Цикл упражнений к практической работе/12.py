N = input()
a = list(map(int, input().split()))
median = a[0]
number = 0
while number != N//2:
    for i in range(N):
