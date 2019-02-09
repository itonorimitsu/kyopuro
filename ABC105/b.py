N = int(input())
judge = False
for i in range(0, 25):
    for j in range(0, 14):
        if (i * 4 + j * 7) == N:
            judge = True
            break
if judge:
    print("Yes")
else:
    print("No")