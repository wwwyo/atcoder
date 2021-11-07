# 2 * 10^5
n,m = map(int,input().split())
mod = 998244353

edge = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(lambda x:int(x)-1,input().split())
    edge[u].append(v)
    edge[v].append(u)

cnt = 0
