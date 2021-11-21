# # 2×10 ^5
# n = 1048576
# a = [-1] * (n+1)
# q = int(input())

# class UnionFind():
#     def __init__(self,n):
#         self.parents = [i for i in range(n+1)]

#     # 所属グループを返す
#     def find(self,i):
#         if self.parents[i] == i:
#             return i
#         else:
#             # 経路の最適化（経路圧縮）
#             self.parents[i] = self.find(self.parents[i])
#             return self.parents[i]

#     def same(self,start,end):
#         return self.find(start) ==  self.find(end)

#     # 親の統一 a => b
#     def unite(self,start,end):
#         i = self.find(start)
#         self.parents[i] = self.find(end)

#     def debug(self):
#         for i in self.parents:
#             print(i)
# # after = [i for i in range(n+1)]
# # prev = [i for i in range(n+1)]
# union = UnionFind(n)

# for _ in range(q):
#     t,x = map(int,input().split())
#     mod = x%n
#     if t == 1:
#         if a[mod] != -1:
#             mod = union.find(mod)

#         a[mod] = x
#         union.unite(mod,(mod+1)%n)
#     else:
#         print(a[mod])

n = 2**20
parent = [-1] * n

def find(x):
    if parent[x] == -1:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def merge(x,y):
    parent[x] = find(y)


q = int(input())
a = [-1] * n
for _ in range(q):
    t,x = map(int,input().split())
    mod = x % n
    if t == 1:
        renew = find(mod)
        a[renew] = x
        if renew == n-1:
            merge(renew,0)
        else:
            merge(renew,renew+1)

    else:
        print(a[mod])