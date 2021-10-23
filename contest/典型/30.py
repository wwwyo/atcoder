# エストラテネスで素因数列挙すれば、O(N log(log(N)))

# * 試し割りだと無理だった
import math
# n = 10 ^ 7
# 1 <= k <= 8
n, k = map(int, input().split())

# 方針
# nをループで回して素数じゃなかったらcontinue
# * 素数かどうかはそれより小さい値の倍数に含まれていないことから確認できる
# 素数なら、倍数をインクリメント
# 最終的なカウントを見れば、その値の素因数の数がわかる

cnt = [0] * (n+1)
for i in range(2,n+1):
    if cnt[i]: continue

    for j in range(i, n+1, i):
        cnt[j] += 1

print(sum(i >= k for i in cnt))
