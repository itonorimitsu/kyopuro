import math

def calc(array):
    min = array[0]
    for i in range(1, len(array)):
        min = int(min * array[i] / math.gcd(min, array[i]))
    return min - 1

if __name__ == "__main__":        
    N = int(input())
    array = list(map(int, input().split()))
    # num = reduce(lcm_base, array, 1) - 1
    num = calc(array)
    count = 0
    for i in range(0, N):
        count += num % array[i]
    print(count)