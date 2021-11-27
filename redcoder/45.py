import math

def round256(y):
    # yの値は0~255に収まる
    if y < 0:
        return 0
    elif y > 255:
        return 255
    else:
        return y

# 差の二乗和を出力
def main(n,m):
    c = [int(input()) for _ in range(m)]
    x = [int(input()) for _ in range(n)]
    y_max = 256

    # i番目の入力においてj番目のcodeで変換したy値との二乗誤差をdp
    dp = [[math.inf] * y_max for _ in range(n)]
    for i in range(n):
        if i == 0:
            y = 128
            for j in range(m):
                y_next = round256(y + c[j])
                dp[i][y_next] = (x[i]-y_next)**2
            continue

        # 前の値
        for y in range(y_max):
            if dp[i-1][y] == math.inf:
                continue

            for j in range(m):
                y_next = round256(y + c[j])
                dp[i][y_next] = min(dp[i][y_next], dp[i-1][y] + (x[i]-y_next)**2)
    print(min(dp[n-1]))

if __name__ == '__main__':
    while True:
        n,m = map(int,input().split())
        if n == m == 0:
            break
        # 圧縮する入力信号の数, コードブックの数
        # 10^4, 16
        main(n,m)