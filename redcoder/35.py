n,col = map(int,input().split())

dp = [[0] * (col+1) for _ in range(n+1)]
for i in range(1,n+1):
    v,w = map(int,input().split())
    for j in range(1,col+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# print(dp)
print(dp[n][col])