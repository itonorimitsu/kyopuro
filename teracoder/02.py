N = int(input())
time = [int(input()) for i in range(N)]
for i in range(0, N):
    day = time[i] // 24
    hour = time[i] % 24
    # print ('日 ' + str(day) + '時間 ' + str(hour))
    print('Case #' + str(i+1) + ':')
    if (hour > 10):
        print((day + 1) * 1000)
    else:
        print(day*1000 + hour*100)

