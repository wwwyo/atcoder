# 200
d,n = map(int,input().split())
temperature = [int(input()) for _ in range(d)]
clothes = [tuple(map(int,input().split())) for _ in range(n)]

# i日目に服jを選んだ派手さ
dp = [[-1] * n for _ in range(d)]

for i in range(d):
    for j in range(n):
        low,high,val = clothes[j]
        if not (low <= temperature[i] <= high):
            continue
        if i == 0:
            dp[i][j] = 0
            continue

        # 前日選んだ服との派手さの絶対値を足す
        for j_1 in range(n):
            if dp[i-1][j_1] == -1:
                continue
            dp[i][j] = max(dp[i][j], abs(val-clothes[j_1][2])+dp[i-1][j_1])

print(max(dp[d-1]))

