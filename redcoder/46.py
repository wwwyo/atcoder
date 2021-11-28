import math
n = int(input())
a = [tuple(map(int,input().split())) for _ in range(n)]

# i番目からj番目までの行列をかけた時の最小コスト
# 一回の行列の積の計算量は(p,q), (q,r) = p*q*r
dp = [[math.inf]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

# l: iとjの差分
# for l in range(1,n):
#     for i in range(n-l):
#         j = i+l
#         for k in range(i,j):
#             dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+(a[i][0]*a[j][0]*a[j][1]))
        
for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+(a[i][0]*a[k][1]*a[j][1]))


print(dp[0][-1])
