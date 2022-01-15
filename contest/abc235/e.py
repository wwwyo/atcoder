
import sys
sys.setrecursionlimit(10**7)
# 10**5
n,m,q = map(int,input().split())
dist = []
for _ in range(m):
    a,b,c = map(int,input().split())
    dist.append((c,a-1,b-1))
dist.sort()

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.memo = {}

    def find(self,x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self,x,y, cost):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            self.parents[x] = self.parents[y]
            self.memo[(x,y)] = cost

    def same(self,x,y):
        return self.find(x) == self.find(y)

uf = UnionFind(n)
# cost = 0
dist_num = 0
for i in range(m):
    c,a,b = dist[i]
    if uf.same(a,b):
        continue
    uf.unite(a,b,c)
    # cost += c
    dist_num += 1
    if dist_num >= n:
        break

print('u')
for _ in range(q):
    print(q)
    u,v,w = map(int,input().split())
    u-=1
    v-=1
    if uf.memo[u,v] > w:
        print('Yes')
    else:
        print('No')









