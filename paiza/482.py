from collections import deque

def bfs(dist, s):
    q = deque([s])
    visited = [[0] * w for _ in range(h)]
    visited[s[0]][s[1]] = 1
    d = [(1,0), (0,1), (-1,0), (0,-1)]
    while q:
        c_x,c_y = q.pop()
        for dx,dy in d:
            x,y = c_x+dx, c_y+dy
            if not (0 <= x < h and 0 <= y < w):
                return True
            if dist[x][y] == '#':
                continue
            if visited[x][y]:
                continue
            visited[x][y] = 1
            q.append((x,y))
    return False




if __name__ == '__main__':
    h,w = map(int,input().split())
    dist = []
    for i in range(h):
        s = list(input())
        if 'S' in s:
            start = (i, s.index('S'))
        dist.append(s)
    if (bfs(dist, start)):
        print('YES')
    else:
        print('NO')
