# 100,10**4
n,w = map(int,input().split())
dp = [[0] * (w+1) for _ in range(n+1)]
for i in range(1,n+1):
    v,w_ = map(int,input().split())
    for j in range(1,w+1):
        if j < w_:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-w_]+v)
print(dp[i][j])
