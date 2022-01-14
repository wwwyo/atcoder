
# 1...n
n,m = map(int,input().split())
mod = 10**5
s = [0] * (n)
for i in range(1,n):
    s_i = int(input())
    s[i] = s_i + s[i-1]

ans = 0
now = 0
for i in range(m):
    a = int(input())
    ans = (ans + abs(s[now+a] - s[now])) % mod
    now += a

print(ans)



