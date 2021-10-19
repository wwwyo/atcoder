import math
from itertools import permutations
# n = 10
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# m = 45
m = int(input())
dislike = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    dislike[x].append(y)
    dislike[y].append(x)

ans = math.inf
# 全探索で嫌いな奴いたら除外する
for comb in permutations(range(n)):
    time = 0
    runner = -1
    # j区間、i人目
    for j, i in enumerate(comb):
        time += a[i][j]
        if runner in dislike[i]:
            break
        runner = i
    else:
        ans = min(ans, time)

if ans == math.inf:
    print(-1)
else:
    print(ans)
