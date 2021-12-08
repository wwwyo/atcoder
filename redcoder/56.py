# 10^5
v,e,r = map(int,input().split())
dist = [[] for _ in range(v)]
for _ in range(e):
    s,t,d = map(int,input().split())
    dist[s].append(t)