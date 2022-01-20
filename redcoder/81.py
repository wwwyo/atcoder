
# 10**5
from itertools import accumulate

n = int(input())
colors = [0] * (10**6+2)
for _ in range(n):
    a,b = map(int,input().split())
    colors[a] += 1
    colors[b+1] -=1

print(max(accumulate(colors)))
