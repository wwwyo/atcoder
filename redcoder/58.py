
# ! timeout
from collections import deque
import heapq
# 10^5,10^5,n-2,10^5
n,m,k,s = map(int,input().split())
# 安い、高い
price = list(map(int,input().split()))
cost = [0]*n
zonbi = {}
for _ in range(k):
    zonbi[int(input())-1] = 1

dist = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(lambda x: int(x)-1,input().split())
    dist[a].append(b)
    dist[b].append(a)

# 宿泊費の合計の最小値
# 1. 幅優先探索で高くなる町(s以内)をpick up
# 2. dijkstraでnまでの最小のコストを求める
def bfs(start,visited):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    step = 0
    while step <= s:
        for _ in range(len(queue)):
            current = queue.popleft()
            cost[current] = 1
            for next in dist[current]:
                if visited.get(next):
                    continue
                visited[next] = 1
                queue.append(next)
        step +=1


def dijkstra(start,end,visited):
    queue = [[0,start]]
    while queue:
        curr_cost,current = heapq.heappop(queue)
        if visited.get(current):
            continue
        if current == end:
            return curr_cost-price[cost[current]]
        for next in dist[current]:
            if visited.get(next):
                continue
            heapq.heappush(queue,[price[cost[next]]+curr_cost,next])



for i in zonbi.keys():
    # costをセットしていく
    bfs(i,zonbi.copy())

print(dijkstra(0,n-1,zonbi.copy()))

