
# https://www.youtube.com/watch?v=TdR816rqc3s&t=6822s
# !連結判定はUnion-Find
# Unionはnodeをグルーピングする
# Findはどのグループに属するか？
# O(log(N)) or O(a(N))(小さい方をくっつける&経路縮約)



# h,w = 10 ** 3
# q = 10**5
# h行w列の色を管理する
# 白=>0,赤=>1

h,w = map(int,input().split())
q = int(input())


#!TLE 色を管理する2次元表に外枠を作る=>上下左右のout of rangeを防ぐ
# colors = [[0] * (w+2) for _ in range(h+2)]
# def is_arrive_bfs(start,goal):
#     if start == goal:
#         return True
#     global colors
#     visited = set()
#     queue = []

#     visited.add(start)
#     queue.append(start)

#     d = [(1,0),(-1,0),(0,1),(0,-1)]
#     for x,y in queue:
#         for dx,dy in d:
#             coordinate = (x+dx,y+dy)
#             if coordinate == goal:
#                 return True
#             if colors[x + dx][y+ dy] == 1 and (not coordinate in visited):
#                 visited.add(coordinate)
#                 queue.append(coordinate)
#     return False


class UnionFind():
    def __init__(self,h,w):
        self.parents = [[(x,y) for y in range(w+1)] for x in range(h+1)]

    # 所属グループを返す
    def find(self,coordinate):
        x,y = coordinate
        if self.parents[x][y] == coordinate:
            return coordinate
        else:
            # 経路の最適化（経路圧縮）
            self.parents[x][y] = self.find(self.parents[x][y])
            return self.parents[x][y]

    def same(self,start,end):
        return self.find(start) ==  self.find(end)

    # 親の統一 a => b
    def unite(self,start,end):
        x,y = self.find(start)
        self.parents[x][y] = self.find(end)

    def debug(self):
        for i in self.parents:
            print(i)




uf = UnionFind(h,w)
colors = [[0] * (w+2) for _ in range(h+2)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        r,c = q[1:]
        colors[r][c] = 1
        for dx,dy in d:
            x = r+dx
            y = c+dy
            if colors[x][y] == 1:
                uf.unite((r,c),(x,y))
    else:
        ra,ca,rb,cb = q[1:]
        if colors[ra][ca] == colors[rb][cb] == 1:
            if uf.same((ra,ca),(rb,cb)):
                print('Yes')
                continue

        print('No')


