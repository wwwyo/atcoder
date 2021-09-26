n = int(input())
a = list(map(int,input().split()))

pattern = []
pattern.append(a[0])
cnt = [0] * 10
cnt[a[0]] = 1
# i番目までのパターンを計算する
for i in range(1,n):
    new_pattern = []
    new_cnt = [0] * 10
    y = a[i]

    for x in pattern:

        sum_ = (x + y) % 10
        multi_ = (x * y) % 10

        if not sum_ in new_pattern:
            new_pattern.append(sum_)
        new_cnt[sum_] = (new_cnt[sum_] + cnt[x]) % 998244353

        if not multi_ in new_pattern:
            new_pattern.append(multi_)
        new_cnt[multi_] = (new_cnt[multi_] + cnt[x]) % 998244353
    pattern = new_pattern
    cnt = new_cnt


for i in cnt:
    print(i % 998244353)