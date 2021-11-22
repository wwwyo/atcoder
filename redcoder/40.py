# n = 100
# 3日以上同じものは並ばない
mod = 10000
n,k = map(int,input().split())


def eatDp(i,j):
    for k in range(3):
        if j == k:
            dp[i][j][k] += dp[i-1][k][(k-1)%3] % mod
            dp[i][j][k] += dp[i-1][k][(k-2)%3] % mod
        else:
            # 全部違うやつ
            dp[i][j][k] += dp[i-1][k][3-j-k] %mod
            # 2個被り
            dp[i][j][k] += dp[i-1][k][j]%mod
            dp[i][j][k] += dp[i-1][k][k]%mod


# i日目j,i-1日目にkを食べる
dp = [[[0] *3 for _ in range(3)] for _ in range(n)]
decide_menu = [-1] * n

for _ in range(k):
    a,b = map(lambda x:int(x)-1,input().split())
    decide_menu[a] = b

# 初期値
for j in range(3):
    for k in range(3):
        j_decide,k_decide = decide_menu[1],decide_menu[0]
        if j_decide != -1 and k_decide != -1:
            if not (j_decide == j and k_decide == k):
                continue
        elif j_decide == -1 and k_decide != -1:
            if not k_decide == k:
                continue
        elif j_decide != -1 and k_decide == -1:
            if not j_decide == j:
                continue
        dp[1][j][k] = 1

for i in range(2,n):
    menu = decide_menu[i]
    if menu != -1:
        eatDp(i,menu)
    else:
        for j in range(3):
            eatDp(i,j)

print(sum(sum(dp[n-1],[]))%mod)

