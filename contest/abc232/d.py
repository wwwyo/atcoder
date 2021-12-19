from collections import deque

# 行列
# 100

def dfs(x,y):
    if memo[x][y]:
        return memo[x][y]
    d = [(1,0),(0,1)]
    # print(x,y)
    step = 0
    for dx,dy in d:
        if not(0 <= x+dx < h and 0 <= y+dy < w):
            continue
        if c[x+dx][y+dy] == '#':
            continue
        step = max(step,dfs(x+dx,y+dy))
    memo[x][y] = 1+step
    return 1+step



if __name__ == '__main__':
    h,w = map(int,input().split())
    c = []
    for _ in range(h):
        c.append(list(input()))
    memo = [[0] * w for _ in range(h)]
    print(dfs(0,0))
    # print(memo)


