import sys
import math
sys.setrecursionlimit(10**7)

# 16
n,m = map(int,input().split())

# sをすでに探索済みの時、tから元の位置に戻る
dist_time = [[math.inf] * (n) for _ in range(n)]
for _ in range(m):
    s,t,d,time = map(int,input().split())
    s-=1
    t-=1
    dist_time[s][t] = (d,time)
    dist_time[t][s] = (d,time)

# 探索時間をメモ
dp = [[-1] * n for _ in range(2**n)]
paths = [[-1] * n for _ in range(2**n)]
def dfs(visited, current):
    # メモ済み
    if dp[visited][current] != -1:
        return dp[visited][current]
    # 全探索して最初に戻ってきたら
    if visited == (2**n)-1 and current==0:
        dp[visited][current] = 0
        paths[visited][current] = 1
        return 0

    res = math.inf
    for next in range(n):
        # 探索済み
        if visited>>next &1:
            continue

        dist = dfs(visited|1<<next,next)
        if dist == math.inf:
            continue
        dist += dist_time[current][next][0]

        # 無向グラフだからこれで良い
        if dist > dist_time[current][next][1]:
            continue
        
        if res > dist:
            res = dist
            paths[visited][current] = paths[visited|1<<next][next]
        elif res == dist:
            paths[visited][current] += paths[visited|1<<next][next]
    return res

ans = dfs(0,0)
if ans == math.inf:
    print('IMPOSSIBLE')
else:
    print(ans,paths[0][0])






