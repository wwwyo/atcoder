from collections import deque
# h,w = max(16)
h,w = map(int,input().split())
dist = []
for _ in range(h):
    c = list(map(lambda x: 1 if x == '.' else 0,list(input())))
    dist.append(c)

def recursive(start, cur, visited):
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    step = 1
    for dx,dy in d:
        x = dx + cur[0]
        y = dy + cur[1]
        if not(0 <= (x) < h and 0 <= (y) < w):
            continue
        elif (not dist[x][y]):
            continue
        elif (x,y) == start:
            # 基底
            step = max(step, len(visited))
        elif not (x,y) in visited:
            step = max(step, recursive(start,(x,y),visited | {(x,y)}))
    return step


ans = 0
for i in range(h):
    for j in range(w):
        # start = i,j
        if not dist[i][j]:
            continue

        ans = max(ans, recursive((i,j), (i,j), {(i,j)}))
if ans < 3:
    print(-1)
else:
    print(ans)

