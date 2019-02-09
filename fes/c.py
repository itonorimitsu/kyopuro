inf = list(map(int, input().split()))
nums = list(map(int, input().split()))
array = []
for i in range(0, inf[0]):
    for j in range(1, inf[1]+1):
        if nums[i] // (2 ** j) == 0 or j == inf[1] - 1:
            print(nums[i] // (2 ** j))
            array.append(j+1)
            break
sum = array[0]
for i in range(1, len(array)):
    sum *= array[i]
print(array)
print(sum)