# 100
# 全探索無理そうだったらdpでメモすることを考える！！！
n = int(input())
arr = list(map(int,input().split()))
ans = arr.pop()

# 左からi番目までとった時に、jとなる数を管理
dp = [[0] * (21) for _ in range(n-1)]
dp[0][arr[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if 0 <= (arr[i] + j) < 21:
            # print(arr[i]+j)
            dp[i][arr[i]+j] += dp[i-1][j]
        if 0 <= (j-arr[i]) < 21:
            dp[i][j-arr[i]] += dp[i-1][j]

print(dp[n-2][ans])
