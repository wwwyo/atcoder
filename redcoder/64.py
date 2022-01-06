# 0から
# 10**4

import heapq

v,e = map(int,input().split())
dist = [[] for _ in range(v)]
for _ in range(e):
    s,t,w = map(int,input().split())
    dist[s].append((t,w))
    dist[t].append((s,w))

visited = [0] * v
connection = 0
q = [(0,0)]
heapq.heapify(q)
ans = 0
while len(q):
    cost,current = heapq.heappop(q)
    if visited[current]:
        continue
    visited[current] = 1
    connection+=1
    ans += cost
    for next, next_cost in dist[current]:
        if visited[next]:
            continue
        heapq.heappush(q,(next_cost,next))

print(ans)



