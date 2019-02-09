A = int(input())
B = int(input())
C = int(input())
S = int(input())
sum = A + B + C
if sum + 3 < S or S < sum:
    print("No")
else:
    print("Yes")