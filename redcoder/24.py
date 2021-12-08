from collections import deque
# n =100
n = int(input())
visited = {}
queue = deque()
g = [[] for _ in range(n)]
step =0


def dfs(current,step):
    if visited.get(current):
        return step-1
    visited[current] = [step,0]
    for next in g[current]:
        step = dfs(next,step+1)
    visited[current][1] = step+1
    return step+1
    


for _ in range(n):
    lst = list(map(int,input().split()))
    u,v = lst[0],lst[1]
    if v != 0:
        g[u-1] = list(map(lambda x: x-1,lst[2:]))

for i in range(n):
    if not visited.get(i):
        step = dfs(i,step+1)
    print(i+1,*visited[i])


