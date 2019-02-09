def calc(num):
    s = []
    for i in range(0, num):
        line = int(input())
        s.append(line)
    s.sort()

    sum_num = 0
    for i in range(1, num-1):
        sum_num += s[i]

    # print(s)
    print(int(sum_num / (num - 2)))


while(1):
    num = int(input())
    if num == 0: break
    calc(num)
