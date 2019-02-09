array = list(map(int, input().split()))
array.sort()

count=0
for i in range(1, len(array)):
    count += array[i] - array[i-1]
print(count)