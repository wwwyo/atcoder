import math
import heapq
# 100,5000
n,k = map(int,input().split())
dist = [[] for _ in range(n)]

def dijkstra(start,goal):
    queue = [(0,start)]
    visited = [math.inf] * n
    while queue:
        current_cost, current = heapq.heappop(queue)
        if current == goal:
            return current_cost
        if visited[current] != math.inf:
            continue
        visited[current] = current_cost
        for next,next_cost in dist[current]:
            if visited[next] != math.inf:
                continue
            heapq.heappush(queue,[current_cost + next_cost, next])
    return -1

for _ in range(k):
    lst = list(map(lambda x: int(x)-1,input().split()))
    if lst[0] == -1:
        print(dijkstra(*lst[1:]))
    elif lst[0] == 0:
        a,b,c = lst[1:]
        c+=1
        dist[a].append([b,c])
        dist[b].append([a,c])


