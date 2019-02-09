N = int(input())
S = []
M = []
L = []
for i in range(0, N):
    s1, m1, l1 = [str(i) for i in input().split()]
    S.append(s1)
    M.append(m1)
    L.append(l1)
for i in range(0, N):
    print('Case #' + str(i + 1) + ':')
    if (len(S[i]) < 5 or len(M[i]) < 7 or len(L[i]) < 5):
        print('NG')
    else:
        print(S[i][:5] + ' ' + M[i][:7] + ' ' + L[i][:5])
