# https://atcoder.jp/contests/abc211/tasks/abc211_d
# 方針
# 1. 探索するpath
# 2. 頂点1からのstep数を管理、チェックもできる
# 3. 頂点1からのその経路に訪れるルートの数。前の経路のパスと同じ数になる
# 今回は最短経路の数を求めたいから探索済のpathの扱いに注意する
# 前通りとっても O(N+M)
# 各頂点をリストに入れる数はN
# Nからの辺の数だけ計算されるので辺の数M

import sys
# import queue
n,m = map(int,input().split())
ab = [[] for _ in range(n)]

for s in sys.stdin.readlines():
    a,b = map(int,s.split())
    ab[a-1] += [b-1]
    ab[b-1] += [a-1]

step = [None] * n
step[0] = 0
next = []
next.append(0)
cnt = [0] * n
cnt[0] = 1

for v in next:
    for vv in ab[v]:
        # まだ探索してない
        if step[vv] is None:
            step[vv] = step[v]+1
            cnt[vv] = cnt[v]
            next.append(vv)
        elif step[vv] == step[v]+1:
                cnt[vv] += cnt[v]
                cnt[vv] %= 10**9+7
print(cnt[n-1])

#! 速度が遅い
# while not done:
#     new_visited = set()
#     for _ in range(next.qsize()):
#         visit = next.get()

#         for v in ab[visit]:
#             if v == n:
#                 ans+=1
#                 done = True
#             elif not v in visited:
#                 new_visited.add(v)
#                 next.put(v)
#     visited = visited | new_visited
#     if next.empty():
#         done = True

# print(ans)