N = list(map(int, input().split()))
list = []
count = 0
for i in range(0, N[0]):
    S = tuple(input())
    if '#' in S:
        count = count + 1
        list.append(S)
# print(list)
c=0
for i in range(0, N[1]):
    c=0
    for j in range(0, count):
        c = c + 1
        print(list[j][i])
        if list[j][i] == '#':
            break
        elif c == count and list[i][j] != '#':
            for j in range(0, count):
                
print(list)
