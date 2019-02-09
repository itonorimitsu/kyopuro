N = int(input())
for i in range(0, N):
    youso = int(input())
    num = list(map(int, input().split()))
    list = []
    for j in range(0, youso):
        for k in range(j, youso):
            if (not (num[j] + num[k]) in list):
                list.append(num[j]+num[k])

    print('Case #' + str(i + 1) + ':')
    print(list)
    print(sum(list))
