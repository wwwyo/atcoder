import math
# n=60
# x = 10^8
# a_i+1 = a_i * k
n,x = map(int,input().split())
a = list(map(int,input().split()))


# # 支払い+お釣り
# dp = [[math.inf]*n ]
# # i番目の円で支払うときの合計の最小値
# dp[0] = x
# for i in range(n):
    # yen = a[i]
    # 限界まで超えない or 1枚分多く超えるで最小値

ans = math.inf
# 限界まで超えない、1枚分多く超えるであまりをメモ
# i枚まで使うときの超えるときの
dp = [[math.inf]*4 for _ in range(n)]

for i in range(n-1,-1,-1):
    coin_num = remain // a[i]
    remain = remain % a[i]
    remain_over = remain - a[i]

    dp[i][0] = coin_num
    dp[i][1] = coin_num+1



