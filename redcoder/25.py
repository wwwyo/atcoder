from collections import deque

# 列、行
def main(w,h):
    dist = []
    for _ in range(h):
        c = list(map(lambda x: 0 if int(x)==1 else 1,input().split()))
        dist.append(c)
    # visited = [[0]*w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if dist[i][j]:
                continue
            bfs(i,j,dist)
            ans+=1
    print(ans)

def bfs(i,j,visited):
    queue = deque([[i,j]])
    visited[i][j] = 1
    d = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)]

    while queue:
        c_i,c_j = queue.popleft()
        for dx,dy in d:
            x = c_i+dx
            y = c_j+dy
            if not(0<=x<h and 0<=y<w):
                continue
            if visited[x][y]:
                continue
            visited[x][y] = 1
            queue.append([x,y])
    
        


if __name__ == '__main__':
    while True:
        w,h = map(int,input().split())
        if w == 0 and h == 0:
            break
        main(w,h)


