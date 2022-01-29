
import sys
sys.setrecursionlimit(10**8)
n,m = map(int,input().split())
edges = []

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.p = [-1] * n

    def find(self,x):
        if self.p[x] <= -1:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        # print(self.p)
        if x == y:
            return
        else:
            if self.p[x] > self.p[y]:
                x,y = y,x
            # xの方が深い
            self.p[x] += self.p[y]
            self.p[y] = x

    def is_connect(self):
        cnt = 0
        for i in range(self.n):
            if self.find(i) == i:
                cnt += 1
                if cnt > 1:
                    return False
        return True

for _ in range(m):
    edges.append(list(map(lambda x:int(x)-1,input().split())))
ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if i == j:
            continue
        a,b = edges[j]
        uf.union(a,b)
    if not uf.is_connect():
        ans+=1

print(ans)
