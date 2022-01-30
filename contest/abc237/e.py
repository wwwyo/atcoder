

import sys
sys.setrecursionlimit(10**8)
n,m = map(int,input().split())
h = list(map(int,input().split()))
dist = [[] for _ in range(n)]
for _ in range(m):
    u,v = map(lambda x: int(x)-1,input().split())
    dist[u].append(v)
    dist[v].append(u)

def recursive(enjoy,node, visited):
    # print(enjoy)
    new_enjoy = enjoy
    for next in dist[node]:
        if next in visited:
            continue
        node_e = h[node]
        next_e = h[next]
        if node_e >= next_e:
            e = node_e - next_e
        else:
            e = -2 * (next_e - node_e)
        # print(node,':',next)
        new_enjoy = max(new_enjoy,recursive(enjoy + e, next, visited | {next}))
        # print(node,':',next,':',e,'-->',enjoy)
    return new_enjoy



enjoy = 0
node = 0
visited = {0}
print(recursive(enjoy, node, visited))



