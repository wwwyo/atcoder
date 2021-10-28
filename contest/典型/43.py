import math
from collections import deque
# Sij #の時壁 . の時壁なし
# max(h,w) = 1000
h,w = map(int,input().split())

s_x,s_y = tuple(map(lambda x: int(x)-1,input().split()))
g_x,g_y = tuple(map(lambda x: int(x)-1,input().split()))
mp = []
for _ in range(h):
    mp.append(list(input()))

def existInRange(x,y):
    return (0 <= (x) < h and 0 <= (y) < w)

dist = [[math.inf for _ in range(w)] for _ in range(h)]

dist[s_x][s_y] = 0
queue = deque()
# 上,右,下,左
d = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(4):
    dx,dy = d[i]
    xx = s_x + dx
    yy = s_y + dy
    if not existInRange(xx,yy): continue
    # 行、列、コスト、方向
    queue.append((s_x,s_y,0,i))

while len(queue):
    x,y,cost,direct = queue.popleft()
    for i in range(4):
        dx,dy = d[i]
        xx = x + dx
        yy = y + dy

        if not existInRange(xx,yy): continue
        if mp[xx][yy] == '#': continue

        # 計算量落としている
        if direct == i:
            if dist[xx][yy] >= cost:
                dist[xx][yy] = cost
                queue.appendleft((xx,yy,cost,i))
        else:
            if dist[xx][yy] >= cost+1:
                dist[xx][yy] = cost+1
                queue.append((xx,yy,cost+1,i))

print(dist[g_x][g_y])



