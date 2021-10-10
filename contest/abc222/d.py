
# if __name__ == '__main__':
#     # 3000
#     n = int(input())
#     # i <= i+1
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))

#     # a <= c <= b

#     # mod 998244353

#     # i番目にjを選んだ時の最大数を管理=>積

#     cnt = 0
#     dp = [[0] * 3001 for _ in range(n)] #[iを選んだ時,最大数]
#     # 初期値
#     z = 0
#     for i in range(a[0],b[0]+1):
#         z +=1
#         dp[0][i] = z
#     prev_max = b[0]+1
#     prev_min = a[0]
#     # i番目を取り出す

#     for i in range(1,n):
#         for j in range(max(prev_min,a[i]),b[i]+1):
#             cnt = 0
#             if j >= prev_max:
#                 cnt += dp[i-1][prev_max]
#             else:
#                 cnt += dp[i-1][j]
#             dp[i][j] = cnt
#         prev_min = a[i]
#         prev_max = b[i]+1

#     print(dp)
#     print(sum(dp[n-1]) % 998244353)



mod = 998244353
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# i番目にjを選ぶ
m = 3000
# i番目にjを選んだ時の最大数
dp = [1] * (m+1)
for i in range(n):
    # i番目にjを選んだ時のi-1番目のjのコピー
    nx = [0] * (m+1)
    for j in range(a[i], b[i]+1):
        nx[j] = dp[j]
    dp = nx
    for i in range(m):
        dp[i+1] = (dp[i+1] + dp[i]) % mod
print(dp[m])

