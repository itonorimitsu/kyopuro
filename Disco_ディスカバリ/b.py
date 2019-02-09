N = int(input())
if(N % 2 ==1):
    num = (N - 2)** 2//2+1
    print(num)
else:
    num = (N ** 2 - 2 * N) // 2
    print(num)