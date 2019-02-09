import math

def make_prime_list_2(num):
    if num < 2:
        return []

    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]

if __name__ == "__main__":
    N = int(input())
    if (N < 105):
        print(0)
    elif (N < 107):
        print(1)
    else:
        c = 1
        for j in range(107, N+1):
            num = j
            num_sqrt = math.floor(math.sqrt(num))
            prime_list = make_prime_list_2(num_sqrt)

            divisor_num = 1
            for prime in prime_list:
                count = 1
                while num % prime == 0:
                    num //= prime
                    count += 1
                divisor_num *= count
            if num != 1:
                divisor_num *= 2

            if divisor_num == 8 and j % 2 == 1:
                c = c + 1

            if j == N:
                print(c)