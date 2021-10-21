# max(n) = 10^5
n, k = map(int, input().split())

# ai = 10 * 9
a = list(map(int, input().split()))

kind = 0
cnt = 0
memo = {}
max_ = 0
for i in range(n):
    if not memo.get(a[i]):
        memo[a[i]] = 1
        kind += 1
    else:
        memo[a[i]] += 1
    cnt += 1

    if kind == k:
        max_ = max(max_, cnt)
    elif kind > k:
        while kind > k:
            start = a[i+1 - cnt]
            memo[start] -= 1
            cnt -= 1
            if memo[start] == 0:
                kind -= 1
max_ = max(max_, cnt)
print(max_)
