import heapq
# 10^5
v,e,r = map(int,input().split())
dist = [[] for _ in range(v)]
for _ in range(e):
    s,t,d = map(int,input().split())
    dist[s].append((t,d))

seen = ["INF"] * v
queue = [(0,r)]

while len(queue):
    curr_cost,current = heapq.heappop(queue)
    if seen[current] != "INF":
        continue
    seen[current] = curr_cost
    for next,next_cost in dist[current]:
        if seen[next] != "INF":
            continue
        heapq.heappush(queue,(next_cost + curr_cost,next))

print(*seen,sep="\n")

