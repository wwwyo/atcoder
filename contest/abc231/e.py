# import math
# # n=60
# # x = 10^8
# # a_i+1 = a_i * k
# n,x = map(int,input().split())
# a = list(map(int,input().split()))

# # # 支払い+お釣り
# # dp = [[math.inf]*n ]
# # # i番目の円で支払うときの合計の最小値
# # dp[0] = x
# # for i in range(n):
#     # yen = a[i]
#     # 限界まで超えない or 1枚分多く超えるで最小値

# ans = math.inf
# # 限界まで超えない、1枚分多く超えるであまりをメモ
# # i枚まで使うときの超えるときの
# dp = [[math.inf]*4 for _ in range(n)]

# for i in range(n-1,-1,-1):
#     coin_num = remain // a[i]
#     remain = remain % a[i]
#     remain_over = remain - a[i]

#     dp[i][0] = coin_num
#     dp[i][1] = coin_num+1



# n,x = map(int,input().split())
# a = list(map(int,input().split()))
# dicts = [dict() for _ in range(n)]

# def solve(x,i):
#     old_x = x
#     if x in dicts[i]:
#         return dicts[i][x]

#     cost = x//a[i]
#     x %= a[i]
#     if x == 0:
#         return cost
#     # 普通に計算する時, 1+多くする時
#     cost += min(solve(x,i-1), 1+solve(a[i]-x,i-1))
#     # メモ化
#     dicts[i][old_x] = cost
#     return cost

# print(solve(x,n-1))


# ギリギリまで払うかギリギリまで払って+1したときの最小値を再帰で呼び出す
n,x = map(int,input().split())
a = list(map(int,input().split()))
# i番目のお金を使った時、残りxだったときの（支払い＋お釣り）最小値
memo = [{} for _ in range(n)]

def solve(x,i):
    old_x = x
    if x in memo[i]:
        return memo[i][x]

    cost = x//a[i]
    x %= a[i]

    if x != 0:
        cost += min(solve(x,i-1),1+solve(a[i]-x,i-1))
    memo[i][old_x] = cost
    return cost
print(solve(x,n-1))