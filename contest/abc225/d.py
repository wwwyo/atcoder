# class UnionFind():
#     def __init__(self,n):
#         self.parents = [i for i in range(n+1)]
#         self.memo = [0] * (n+1)

#     # 所属グループを返す
#     def find(self,x):
#         if self.parents[x] == x:
#             return x
#         else:
#             # 経路の最適化（経路圧縮）
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def same(self,start,end):
#         return self.find(start) ==  self.find(end)

#     # 親の統一 a => b
#     def unite(self,start,end):
#         x = self.find(end)
#         self.parents[x] = self.find(start)
#         self.memo[start] = end
#         # print(self.memo)

#     def remove(self,start,end):
#         self.parents[end] = end
#         self.memo[start] = 0
#         e = end
#         while self.memo[e]:
#             e = self.memo[e]
#             self.parents[e] = end

#     def output(self,start):
#         x = self.find(start)
#         lst = [x]
#         # print('output')

#         # print('start',x)
#         # print('memo',self.memo)
#         while self.memo[x]:
#             x = self.memo[x]
#             lst.append(x)

#         # print('output')
#         print(len(lst),end=" ")
#         print(*lst,sep=" ")


# # n,q = 10**5
# n,q = map(int,input().split())
# union_find = UnionFind(n)
# for _ in range(q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         x,y = query[1],query[2]
#         union_find.unite(x,y)
#     elif query[0] == 2:
#         x,y = query[1],query[2]
#         union_find.remove(x,y)
#     elif query[0] == 3:
#         x = query[1]
#         union_find.output(x)




n,q = map(int,input().split())
# 後ろの電車
next = [0] * (n+1)
# 前の電車
prev = [0] * (n+1)

for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x,y = query[1:]
        next[x] = y
        prev[y] = x
    elif query[0] == 2:
        x,y = query[1:]
        next[x] = 0
        prev[y] = 0
    elif query[0] == 3:
        x = query[1]
        while prev[x]:
            x = prev[x]
        ans = [x]
        while next[x]:
            x = next[x]
            ans.append(x)
        print(len(ans),*ans,sep=" ")

