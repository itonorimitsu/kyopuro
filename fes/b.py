nums = list(map(int, input().split()))
array = []
for i in range(0, nums[1]):
    num = list(map(int, input().split()))
    for j in range(num[0], num[1] + 1):
        if j not in array:
            array.append(j)
array.sort()
print(nums[2]*len(array) + nums[3]*(nums[0]-len(array)))