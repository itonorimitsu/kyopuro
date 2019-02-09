N = int(input())
grade = [int(input()) for i in range(N)]
for i in range(0, N):
    print('Case #' + str(i+1) + ':')
    if grade[i] >= 2019 or grade[i] <= 2007:
        print('NG')
    elif grade[i] < 2018:
        print('CSE')
    else:
        print('ISE')
