from collections import deque
# Sij #の時壁 . の時壁なし
# max(h,w) = 1000
h,w = map(int,input().split())


start = tuple(map(lambda x: int(x)-1,input().split()))
goal = tuple(map(lambda x: int(x)-1,input().split()))
cnt = 0
dist = []

for _ in range(h):
    dist.append(list(input()))

queue = deque()
visited = {}
queue.append(start)
visited[start] = 1

d = [[1,0],[0,1],[-1,0],[0,-1]]
while len(queue):
    x,y = list(queue.popleft())
    print(x,y)
    if (x,y) == goal:
        print(cnt)
        break
    new_queue = deque()
    for dx,dy in d:
        if not(0 <= (x+dx) < h and 0 <= (y+dy) < w): continue
        next = dist[x+dx][y+dy]
        if next == '#': continue
        if visited.get((x+dx,y+dy)):
            continue
        else:
            visited[(x+dx,y+dy)] = 1
        new_queue.append([x+dx,y+dy])
    cnt += 1
    queue = new_queue



