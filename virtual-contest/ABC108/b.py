nums = list(map(int, input().split()))
x = (nums[2] - nums[0])
y = (nums[3] - nums[1])
# kyori = sqrt((x*x) + (y*y))
n1 = nums[2] - y
n2 = nums[3] + x
print(n1, end="")
print(" ", end="")
print(n2, end="")
print(" ", end="")
print(n1 - x, end="")
print(" ", end="")
print(n2 - y)