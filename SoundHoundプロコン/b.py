s = list(input().strip())
w = int(input())
ans = ""
for i in range(0, len(s)):
    if(i % w == 0):
        ans += s[i]
print(ans)