# 2ツ並んだブロックの差が1なら落とせる
# 取り除けるブロックの個数
# n:300
def main(n):
    w = list(map(int,input().split()))
    # まず、2つ並びのブロックが落とせるかチェックする0,1
    # 間隔を広げていくdp
    # 区間[ij]に置いて操作を施せる最大の回数
    dp = [[0] * n for _ in range(n)]
    # ブロックの数
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if l %2 ==0:
                # 両端を残して全部消えるかを判定
                if dp[i+1][j-1] == l-2 and abs(w[i]-w[j]) <2:
                    dp[i][j] = l
                else:
                    for k in range(i+1,j):
                        dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
            else:
                # 最善の偶数のパターンを返す
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    print(dp[0][-1])



if __name__ == '__main__':
    while True:
        n = int(input())
        if n ==0:
            break
        main(n)