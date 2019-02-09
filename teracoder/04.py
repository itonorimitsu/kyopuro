import math

N = int(input())
a = []
b = []
for i in range(N):
    a1, b1 = [int(i) for i in input().split()]
    a.append(a1)
    b.append(b1)
for i in range(0, N):
    print('Case #' + str(i + 1) + ':')
    print((a[i] * b[i]) // math.gcd(a[i], b[i]))