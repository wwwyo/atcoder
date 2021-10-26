# 9の性質
# x mod 9 = xの各桁の和 mod 9
# ①Nが9の倍数でなければ0
# ②全ての「各位の数字の和がkとなる整数」が9の倍数となるため、答えは各位の数字の輪がkである生成数の個数
mod = 10**9+7
# max(k) = 10^5
k = int(input())
if k % 9 != 0:
    print(0)
    exit()

# kであることが担保されている
# dp[k-(1~9))] + [1 ~ 9] => k
# iを満たす数の総数
dp = [0] * (k+1)
dp[0] = 1
for i in range(1, k+1):
    num = min(9, i)
    for j in range(1, num+1):
        dp[i] += dp[i-j]
    dp[i] %= mod

print(dp[k])
# 和がkになる組み合わせ
