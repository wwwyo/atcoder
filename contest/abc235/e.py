
import sys
sys.setrecursionlimit(10**5)
# # 10**5
# n,m,q = map(int,input().split())
# dist = []
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     dist.append((c,a-1,b-1))
# dist.sort()

# class UnionFind:
#     def __init__(self,n):
#         self.n = n
#         self.parents = [i for i in range(n)]
#         self.memo = {}

#     def find(self,x):
#         if self.parents[x] == x:
#             return x
#         self.parents[x] = self.find(self.parents[x])
#         return self.parents[x]

#     def unite(self,x,y, cost):
#         x = self.find(x)
#         y = self.find(y)
#         if x == y:
#             return
#         else:
#             self.parents[x] = self.parents[y]
#             self.memo[(x,y)] = cost

#     def same(self,x,y):
#         return self.find(x) == self.find(y)

# uf = UnionFind(n)
# # cost = 0
# dist_num = 0
# for i in range(m):
#     c,a,b = dist[i]
#     if uf.same(a,b):
#         continue
#     uf.unite(a,b,c)
#     # cost += c
#     dist_num += 1
#     if dist_num >= n:
#         break

# print('u')
# for _ in range(q):
#     print(q)
#     u,v,w = map(int,input().split())
#     u-=1
#     v-=1
#     if uf.memo[u,v] > w:
#         print('Yes')
#     else:
#         print('No')



n,m,q = map(int,input().split())

class UnionFind():
    def __init__(self,n):
        # 根が要素数を管理
        self.p = [-1] * (n+1)

    def find(self, x):
        if self.p[x] < 0: return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x,y):

        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # 要素数が多い方の根に結合
        if self.p[x] > self.p[y]:
            x,y = y,x
        # -に増えていく
        self.p[x] += self.p[y]
        self.p[y] = x

    
    def same(self,x,y):
        # print('same!')
        return self.find(x) == self.find(y)


edges = []
for _ in range(m):
    u,v,w = map(int,input().split())
    edges.append((w,u,v,-1))

for i in range(q):
    u,v,w = map(int,input().split())
    edges.append((w,u,v,i))

edges.sort()

ans = [False] * q
uf = UnionFind(n)
for (w, u,v,q) in edges:
    # print(w,u,v,q)
    if uf.same(u,v):
        continue

    if q != -1:
        ans[q] = True
    else:
        uf.union(u,v)

for a in ans:
    if a:
        print('Yes')
    else:
        print('No')
