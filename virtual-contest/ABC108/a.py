K = int(input())
if K % 2 == 0:
    K = K // 2
    print(K * K)
else:
    K = K // 2
    print(K * (K+1))