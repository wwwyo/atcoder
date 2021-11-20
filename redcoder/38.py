# 1000
'''
求めたいもの
部分列の数
i番目まで見た部分列の最大数
'''

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        x = list(input())
        y = list(input())

        dp = [[0] * len(y) for _ in range(len(x))]
        len_x = len(x)
        len_y = len(y)
        for i in range(len_x):
            for j in range(len_y):
                if x[i] == y[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                else:
                    if i == 0 or j == 0:
                        continue
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp[len_x - 1][len_y - 1])