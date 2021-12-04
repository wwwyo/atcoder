import bisect
# 10^4
n = int(input())
c = [int(input()) for _ in range(n)]

# sort済みの配列を見つけるsortされていないnodeを動かす。
# => 最大のsort済み配列を見つけるつまりlis

# sort済みi行配列がある時i行目の最小の値
dp = [c[0]]
for i in range(1,n):
    if c[i] > dp[-1]:
        dp.append(c[i])
    else:
        # dpのi行目の最小値を探して更新する
        idx = bisect.bisect_left(dp,c[i])
        dp[idx] = c[i]
print(n - len(dp))