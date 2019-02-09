def tri(x, n):
    if n == 0: return 1
    value = pow1(x, int(n / 2))
    value *= value
    if n % 2 == 1: value *= x
    return value

if __name__ == "__main__":
    S = tuple(input())
    K = int(input())
    sum = 0
    for i in range(0, len(S)):
        if (S[i] == 1):
            sum = sum + 1
            continue
        num = int(S[i])
        sum += pow(num, 500000000000)
        if sum > K:
            print(S[i])
        print(sum)
        