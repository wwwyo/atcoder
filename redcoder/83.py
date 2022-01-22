
from itertools import accumulate
# 10**5
n,m = map(int,input().split())
p = list(map(int,input().split()))
cost = [0]
for _ in range(n-1):
    # きっぷ、ic,icカード
    cost.append(list(map(int,input().split())))

# 何回乗れば元取れるかメモる
# 乗った回数
train = [0] * (n+1)
prev = p[0]
for i in range(1,m):
    now = p[i]
    if prev < now:
        train[prev] += 1
        train[p[i]] -= 1
    else:
        train[prev] -= 1
        train[p[i]] += 1
    prev = now
train = list(accumulate(train))

ans = 0
for i in range(1,n):
    a,b,c = cost[i]
    cnt = train[i]
    if a*cnt < b*cnt+c:
        ans += a*cnt
    else:
        ans += b*cnt+c

print(ans)


    