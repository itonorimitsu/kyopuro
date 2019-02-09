N = int(input())
count = 0
if N > 100:
    N = N - 100
    count = count + 1
if N > 9:
    N = N - 10
    count = count + 1
if N == 1:
    count = count + 1
print(count)