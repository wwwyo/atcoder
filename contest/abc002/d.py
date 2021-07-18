import itertools

n,m = map(int,input().split())

ans = 1
xy = [list(map(int,input().split())) for _ in range(m)]
# for i in range(m):
#     x,y = map(int,input().split())
#     friends[x -1][y-1] = 1
#     friends[y-1][x-1] = 1

for i in range(2**n):
    groups = []
    for j in range(n):
        if i >> j &1:
            groups.append(j)
    for x,y in itertools.combinations(groups,2):
        if not([x,y] in xy or [y,x] in xy):
            break
    else:
        ans = max(ans,len(groups))
print(ans)