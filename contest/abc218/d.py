# 1.左下と右上の頂点の組み合わせ全探索=>左上と右下に欲しい座標が特定できる
# 2.欲しい座標がN個の点に含まれているか二分探索で確認
# point1:同じ座標のものはない
# point2:長方形は対角の２点が決まれば求めることができる
# point3:二分探索使いたいから与えられた配列をソートしとく => 座標圧縮でより高速にすることも可能

# xが等しい組み合わせを作る=>y軸に並行な組み合わせを考えていく方針だったのですがループ４回で案の定TLE

# 座標の存在チェック（二分探索）
def isExist(lst, wish):
    top = len(lst)-1
    bottom =  0
    while bottom <= top:
        middle = (bottom + top) //2
        if lst[middle][0] > wish[0]:
            top = middle - 1
        elif lst[middle][0] < wish[0]:
            bottom = middle + 1
        else:
            if lst[middle][1] > wish[1]:
                top = middle -1
            elif lst[middle][1] < wish[1]:
                bottom = middle + 1
            else:
                return True
    return False

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
xy.sort()
ans = 0

# 全探索
for i in range(n-1):
    x1, y1 = xy[i]
    for j in range(i+1, n):
        x2, y2 = xy[j]
        # 左下と右上を決める(同軸上にないもの)
        if x1 == x2 or y1 == y2:
            continue
        # 左上と右下で欲しい座標
        wish1 = [x1, y2]
        wish2 = [x2, y1]
        # 存在チェック
        if isExist(xy, wish1) and isExist(xy, wish2):
            ans +=1

# 長方形の組み合わせが重複するので割る2
print(ans//2)


# 座標圧縮
a = [8, 100, 33, 33, 33, 12, 6, 1211]
b = sorted(set(a))
d = {v: i for i,v in enumerate(b)}
print(list(map(lambda x: d[x],a)))
