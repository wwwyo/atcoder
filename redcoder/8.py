import math
# 30
n = int(input())
starts = []
goals = []
for _ in range(n):
    a,b = map(int,input().split())
    starts.append(a)
    goals.append(b)

# start goal の間で探す
ans = math.inf
for i in range(n):
    s = starts[i]
    for j in range(n):
        g = goals[j]
        sum_ = 0
        for k in range(n):
            a,b = starts[k],goals[k]
            sum_ += abs(a-b)+abs(s-a)+abs(g-b)
        ans = min(ans,sum_)



print(ans)