
n,q = map(int,input().split())


class UnionFind():
    def __init__(self,n):
        self.p = [0] * (n)

    def find(self,x):
        if self.p[x] == 0:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x
        if x > y:
            x,y = y,x
        elif x == y:
            y += 1
        self.p[x] = y
        return y

    def same(self,x,y):
        return self.find(x) == self.find(y)

uf = UnionFind(n)
for _ in range(q):
    com,x,y = map(int,input().split())
    if com == 0:
        uf.unite(x,y)
    else:
        if uf.same(x,y):
            print(1)
        else:
            print(0)
