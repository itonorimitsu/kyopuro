S = tuple(input()) # これで文字列を一文字にできる
T = input()

for i in range(0, len(S)):
    word = ''
    for j in range(0, len(S)):
        index = (i + j) % len(S)
        word += S[index]
    if word == T:
        print('Yes')
        break
    elif i == j:
        print('No')
        break
