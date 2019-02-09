import itertools
n = list(map(int, input().split())) # nまで, m個, dの差

ave = 0
for data in itertools.product(range(1, n[0] + 1), repeat=3):
    # print(data)
    beau = 0
    for i in range(0, len(data) - 1):
        if(abs(data[i] - data[i+1]) == n[2]):
            beau += 1
    ave += beau
    # gc.collect()

print(ave / (n[0] ** n[1]))
# killed:9 出ちゃう

