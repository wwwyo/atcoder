from math import factorial
# max(n) = 10**5
n,l = map(int,input().split())
mod = 10**9+7
dp = [0] * (n+1)
dp[0] = 1
# i段目までたどり着く総数
for i in range(1,n+1):
    dp[i] += dp[i-1]
    if i >= l:
        dp[i] += dp[i-l]

    dp[i] %= mod



print(dp[n])



