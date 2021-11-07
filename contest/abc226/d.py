# 2 ~ 500
import math
n = int(input())
dist = []
for _ in range(n):
    xy = tuple(map(int,input().split()))
    dist.append(xy)

memo = {}
for i in range(n):
    x_i,y_i = dist[i]
    for j in range(n):
        if i == j:
            continue
        x_j,y_j = dist[j]
        y_change = y_j - y_i
        x_change = x_j - x_i
        if x_change == 0:
            a = math.inf
        else:
            a = (y_change)/(x_change)
        memo[a] = 1

print(2 * len(memo))
    
