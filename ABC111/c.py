import collections

n = int(input())
nums = list(map(int, input().split()))
array_0 = []
array_1 = []
for i in range(0, len(nums)):
    if i % 2 == 0:
        array_0.append(nums[i])
    else:
        array_1.append(nums[i])
c0 = collections.Counter(array_0)
c1 = collections.Counter(array_1)
count_0 = 0
count_1 = 0

if c0.most_common()[0][1] >= c1.most_common()[0][1]:
    if (len(c0) != 1):
        for i in range(1, len(c0)):
            count_0 += c0.most_common()[i][1]
    if c0.most_common()[0][0] != c1.most_common()[0][0]:
        if (len(c1) != 1):
            for i in range(1, len(c1)):
                count_1 += c1.most_common()[i][1]
    else:
        count_1 = c1.most_common()[0][1]
        for i in range(2, len(c1)):
            count_1 += c1.most_common()[i][1]
else:
    if (len(c1) != 1):
        for i in range(1, len(c1)):
            count_1 += c1.most_common()[i][1]
    if c0.most_common()[0][0] != c1.most_common()[0][0]:
        if (len(c0) != 1):
            for i in range(1, len(c0)):
                # print(c1.most_common()[i][1])
                count_0 += c0.most_common()[i][1]
    else:
        count_0 = c0.most_common()[0][1]
        for i in range(2, len(c0)):
            count_0 += c0.most_common()[i][1]

print(count_0 + count_1)