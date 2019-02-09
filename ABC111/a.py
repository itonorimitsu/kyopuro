n = int(input())
N = str(n)
array = list(map(int, list(N)))
for i in range(0, len(array)):
    if array[i] == 1:
        array[i] = 9
    elif array[i] == 9:
        array[i] = 1
print(array[0], end = '')
print(array[1], end = '')
print(array[2])
