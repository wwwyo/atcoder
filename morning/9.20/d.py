# https://atcoder.jp/contests/abc185/editorial/355
import copy

def checkLand(map_):
    for i in range(10):
        for j in range(10):
            if map_[i][j] == 'o':
                return [i,j]
    return []

def dfs(map_):
    t,l = checkLand(map_)

    stack = set()
    stack.add((t,l))
    while len(stack) > 0:
        i,j = stack.pop()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x = i + dx
            y = j + dy
            if 0 <= x < 10 and 0 <= y < 10:
                if map_[x][y] == 'o':
                    map_[x][y] = 'x'
                    stack.add((x,y))
    if not checkLand(map_):
        return True
    else:
        return False


def exec(a):
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'o':
                continue

            map_ = copy.deepcopy(a)
            map_[i][j] = 'o'
            if dfs(map_):
                return 'YES'
    return 'NO'


if __name__ == '__main__':
    a = [list(input()) for _ in range(10)]
    print(exec(a))
