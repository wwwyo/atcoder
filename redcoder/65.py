# 10**5
n,m,k = map(int,input().split())
dist = []
for _ in range(m):
    a,b,c = map(int,input().split())
    dist.append((c,a-1,b-1))

dist.sort()

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * (n)

    def find(self,x):
        if self.parents[x] == -1:
            return x
        self.parents[x] = self.find(self.parents[x])
    
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            self.parents[x] = self.parents[y]

    def same(self,x,y):
        return self.find(x) == self.find(y)

uf = UnionFind(n)
if k == n:
    print(0)
    exit()
dist_num = 0
ans = 0
for i in range(m):
    c,a,b = dist[i]
    if uf.same(a,b):
        print(a,b)
        continue
    uf.unite(a,b)
    ans += c
    dist_num += 1
    if dist_num == n-k:
        break
print(ans)

# 4 3 1
# 1 2 2
# 2 3 9
# 2 4 5

# 5 6 2
# 1 2 5
# 1 3 3
# 2 3 4
# 2 5 7
# 3 4 6
# 4 5 5