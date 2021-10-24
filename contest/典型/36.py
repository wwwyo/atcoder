
# ! マンハッタン距離は45度回転
# (x1,y1),(x2,y2)のマンハッタン距離は
# |x1-x2| + |y1-y2| <= k => kの正方形が45度傾いた領域を表している
# 展開すると
# x1-x2 + y1-y2 || -(x1-x2) + y1-y2 || (x1-x2) + -(y1-y2) || -(x1-x2) + -(y1-y2)
# = x1 + y1 - (x2 + y2) || -(x1 - y1) + x2-y2 || x1-y1 - (x2-y2) || -(x1 + y1) + x2 + y2

# 一般に原点から45度回転させる公式は
# x = (x - y)
# y = (x + y)
#* 大きさは違うよ

# kの正方形がx軸、y軸に平行になる
# 変形後の座標(x1,y1)(x2,y2) のマンハッタン距離を展開した式に代入すると
# https://kagamiz.hatenablog.com/entry/2014/12/21/213931
# X1 - X2 || - (Y1 - Y2) || Y1 - Y2 || -(X1 + X2)

# つまり45度回転した後の4角の座標とのmaxをとれば良い


# max(n,q) = 10 ** 5
n,q = map(int,input().split())


manhattan = []
X_coordinate = []
Y_coordinate = []
for _ in range(n):
    x,y = map(int,input().split())
    x_45,y_45 = x + y,x-y
    manhattan.append((x_45, y_45))
    X_coordinate.append(x_45)
    Y_coordinate.append(y_45)

X_coordinate.sort()
Y_coordinate.sort()
x_max,x_min = X_coordinate[0],X_coordinate[-1]
y_max,y_min = Y_coordinate[0],Y_coordinate[-1]

for _ in range(q):
    # xy_queryのマンハッタン距離の最大値を出力
    query = int(input()) -1
    x,y = manhattan[query]
    print(max(abs(x - x_max), abs(x - x_min), abs(y - y_max), abs(y - y_min)))
