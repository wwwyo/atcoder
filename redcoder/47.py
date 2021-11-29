# import copy
# # 両端のピースのどちらかが取られている
# # IOIは最も大きいもの
# # ! JOIがとるピースの合計を最大化
# # 2000
# n = int(input())
# a = [int(input()) for _ in range(n)]
# # 円環を潰す
# a += a

# # 残りiからjまでの状態でのJOIの取り分の最大値
# # 円環を潰す
# dp = [[0] * (2*n) for _ in range(2*n)]

# # 最後にピースをとるのがJOIの時
# if n %2 == 1:
#     for i in range(2*n):
#         dp[i][i] = a[i]

# for remain in range(2,n+1): #残っているケーキの量で探索
#     for i in range(n):
#         j = i + remain - 1
#         # JOIがとる番
#         if (n-remain) %2 == 0:
#             dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j-1] + a[j])
#         # IOIがとる番
#         else:
#             if a[i] > a[j]:
#                 dp[i][j] = dp[i+1][j]
#             else:
#                 dp[i][j] = dp[i][j-1]
# print(max(dp[i][i+n-1] for i in range(n)))




n = int(input())
a = [int(input()) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

# 最後がJOI
if n %2 == 1:
    for i in range(n):
        dp[i][i] = a[i]

for remain in range(2, n+1):
    for l in range(n):
        r = l + remain-1
        r%=n
        # JOIのターン
        if (n-remain) %2 == 0:
            dp[l][r] = max(dp[(l+1)%n][r] + a[l], dp[l][r-1]+ a[r])
        else:
            if a[r] > a[l]:
                dp[l][r] = dp[l][r-1]
            else:
                dp[l][r] = dp[(l+1)%n][r]
print(max(dp[i][i-1] for i in range(n)))

