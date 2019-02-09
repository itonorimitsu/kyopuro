nums = list(map(int, input().split()))
count=0
if (nums[1] % 2 == 1):
        count = nums[0] // nums[1]
        print(count ** 3)
else:
    count = nums[0] // nums[1]
    sum = count ** 3
    count=0
    for i in range(1, nums[0]+1):
        if i % nums[1] == (nums[1] / 2):
            count = count + 1
    sum += count**3
    print(sum)