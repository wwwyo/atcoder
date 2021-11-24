import math
# 1000
n,m = map(int,input().split())
distance = [int(input()) for _ in range(n)]
whether = [int(input()) for _ in range(m)]

# 街nにm日目に到着した時の疲労度
dp = [[math.inf] * (m+1) for _ in range(n+1)]
for i in range(n+1):
    bef_min_tire = math.inf
    for j in range(i,m+1):
        # 初期値
        if i == 1:
            dp[i][j] = distance[i-1] * whether[j-1]
            continue

        tire = distance[i-1]*whether[j-1]
        bef_min_tire = min(bef_min_tire,dp[i-1][j-1])
        # 前日までにi-1にたどり着いていなかったらcontinue
        if bef_min_tire == math.inf:
            continue
        dp[i][j] = bef_min_tire + tire

print(min(dp[i]))


