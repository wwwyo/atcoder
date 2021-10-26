# !give up!!!!!!!!!!!!!!!!!!!!!11
import math
# max(w) = 10^4, max(n) = 500
w,n = map(int,input().split())

# (val)
dp = [[-math.inf] * (w+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    # l <= 量 <=  r
    l,r,v = map(int,input().split())
    for j in range(w+1):
        if j < l:
            dp[i][j] = dp[i-1][j]
        elif l <= j:
            dp[i][j] = max(dp[i-1][j], (dp[i-1][j-k] for k in range(l,r) + v))

if dp[n][w]:
    print(dp[n][w])
else:
    print(-1)