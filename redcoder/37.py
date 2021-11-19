# 10^4,20
n,m = map(int,input().split())

c = sorted(list(map(int,input().split())))
min_ = n
dp = [i for i in range(n+1)]
# dp[i]i円の時最小のコイン枚数
for i in range(1,n+1):
    for j in range(m):
        if i < c[j]:
            continue
        dp[i] = min(dp[i], dp[i-c[j]]+1)
# print(dp)
print(dp[n])

# 今i円までの最大値を考える
