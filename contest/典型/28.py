# 領域加算は二次元いもす法
# 10**5
n = int(input())
area = [[0] * 1001 for _ in range(1001)]
# 原点が0,0左上のことに注意
for _ in range(n):
    # 左下、右上
    lx, ly, rx, ry = map(int, input().split())
    # 左下と右上を1にする
    area[ly][lx] += 1
    area[ry][rx] += 1
    # 左上と右下を-１にする
    area[ry][lx] += -1
    area[ly][rx] += -1


ans = [0] * n
for i in range(1000):
    for j in range(1000):
        area[i][j+1] += area[i][j]

for i in range(1000):
    for j in range(1000):
        area[i+1][j] += area[i][j]
        if area[i][j] > 0:
            ans[area[i][j]-1] += 1

print(*ans, sep="\n")
