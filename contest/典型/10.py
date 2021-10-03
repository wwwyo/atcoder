# n = 10**5
# q = 10**5
# output(class1の期末試験の合計,class2の期末試験の合計)


# dp[i][j]で入力を管理
# iクラスのj番までの合計
# O(n + q)


n = int(input())
dp = [[0] * (n+1) for _ in range(2)]
for i in range(1,n+1):
    c,p = map(int,input().split())
    if c == 1:
        dp[0][i] += dp[0][i-1] +p
        dp[1][i] += dp[1][i-1]
    else:
        dp[1][i] += dp[1][i-1] +p
        dp[0][i] += dp[0][i-1]

q = int(input())
for _ in range(q):
    s,e = map(int,input().split())
    a = dp[0][e] - dp[0][s-1]
    b = dp[1][e] - dp[1][s-1]
    print(a,b)
