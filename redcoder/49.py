# ある頂点から出発し、出発点へ戻る
# 格頂点をちょうど1度通る

import math
v,e = map(int,input().split())
cost = [[math.inf] * v for _ in range(v)]
for _ in range(e):
    s,t,d = map(int,input().split())
    cost[s][t] = d

# sに訪問ずみ, 頂点vにいるときの頂点0まで戻るコスト
dp = [[-1] * v for _ in range(2**v)]

def dfs(s,current):
    if dp[s][current] != -1:
        return dp[s][current]
    # 全探索終了
    if (s == (2**v-1) and current == 0):
        return 0

    res = math.inf
    for u in range(v):
        if s>>u &1 == 0: #未訪問
            res = min(res, dfs(s|1<<u,u)+cost[current][u])
    dp[s][current] = res
    return res

ans = dfs(0,0)
if ans == math.inf:
    print(-1)
else:
    print(ans)

