# s = R, B, W, #
# 最小で塗り替えるマスの数
# 1000
import numpy as np
n = int(input())
s = [list(input()) for _ in range(5)]
s = np.transpose(s).tolist()

# n行目まで0~2に揃える時の変更数
dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    memo = [0,0,0]
    for k in range(5):
        color = s[i][k]
        if color == 'R':
            memo[0] += 1
        elif color == 'B':
            memo[1] += 1
        elif color == 'W':
            memo[2] += 1
    for j in range(3):
        num = memo[j]
        if i == 0:
            dp[i][j] = 5-num
        else:
            dp[i][j] = min(dp[i-1][(j-1)%3],dp[i-1][(j-2)%3]) + (5-num)

print(min(dp[n-1]))



