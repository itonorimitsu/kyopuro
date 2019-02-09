def calc(a, b):
    amari = a % b
    return amari

if __name__ == "__main__":
    N = int(input())

    for i in range(1, N):
        juices = list(map(int, input().split()))
        a = juices[0]
        b = juices[1]
        c = juices[2]
        d = juices[3]
        data = a
        while True:
            data = calc(data, b)
            # print(data)
            if data == a:
                print("Yes")
                break
            if data > c:
                print("No")
                break
            elif data <= c:
                data += d
            

            
            


