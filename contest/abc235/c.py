
# 10**5
n,q = map(int,input().split())
a = list(map(int,input().split()))
memo = {}
for i in range(n):
    if not memo.get(a[i]):
        memo[a[i]] = [i+1]
    else:
        memo[a[i]].append(i+1)

for _ in range(q):
    x,k = map(int,input().split())
    if not memo.get(x):
        print(-1)
        continue
    else:
        if len(memo[x]) >= k:
            print(memo[x][k-1])
            continue
        else:
            print(-1)
            continue

