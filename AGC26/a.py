N = int(input())
array = list(map(int, input().split()))

front = array[0]
count = 0
length = len(array)
for i in range(1, len(array)):
    if front == array[i]:
        array[i] = length
        length -= 1
        count += 1
    front = array[i]
print(count)
