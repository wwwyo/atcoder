
from heapq import heappush,heappop
# import sys
# sys.setrecursionlimit(10**8)
# n,m = map(int,input().split())
# h = list(map(int,input().split()))
# dist = [[] for _ in range(n)]
# for _ in range(m):
#     u,v = map(lambda x: int(x)-1,input().split())
#     dist[u].append(v)
#     dist[v].append(u)

# def recursive(enjoy,node, visited):
#     # print(enjoy)
#     new_enjoy = enjoy
#     for next in dist[node]:
#         if next in visited:
#             continue
#         node_e = h[node]
#         next_e = h[next]
#         if node_e >= next_e:
#             e = node_e - next_e
#         else:
#             e = -2 * (next_e - node_e)
#         # print(node,':',next)
#         new_enjoy = max(new_enjoy,recursive(enjoy + e, next, visited | {next}))
#         # print(node,':',next,':',e,'-->',enjoy)
#     return new_enjoy



# enjoy = 0
# node = 0
# visited = {0}
# print(recursive(enjoy, node, visited))

# ! 解き直し
# コストを求めるのは最短経路

n,m = map(int,input().split())
h = list(map(int,input().split()))
dist = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(lambda x: int(x)-1,input().split())
    if h[v] > h[u]:
        v,u = u,v
    diff = h[u] - h[v]
    dist[u].append((v, 0))
    dist[v].append((u, diff))

def dijkstra(s):
    pq = []
    cost = [10**18] *n
    cost[s] = 0
    heappush(pq,(0,s))
    while pq:
        frm_c,frm = heappop(pq)
        if cost[frm] < frm_c:
            continue
        for (to,to_c) in dist[frm]:
            if cost[to] > cost[frm] + to_c:
                cost[to] = cost[frm]+to_c
                heappush(pq,(cost[to],to))
    # print(cost)
    ans = 0
    for i in range(n):
        ans = max(ans, -(-h[0] + cost[i] + h[i]))
    print(ans)


dijkstra(0)