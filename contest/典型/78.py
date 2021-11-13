# 10^5
n,m = map(int,input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(lambda x: int(x)-1,input().split())
    edge[a].append(b)
    edge[b].append(a)

ans = 0
for i in range(n):
    nodes = edge[i]
    cnt = 0
    for j in nodes:
        if i > j:
            cnt+=1
        if cnt >= 2:
            break
    else:
        if cnt == 1:
            ans+=1
print(ans)
