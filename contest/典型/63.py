# 極端に小さいやつがあればそいつを全探索する
# max(h) = 8
# max(w) = 10^4
h,w = map(int,input().split())
grid = []
for _ in range(h):
    p = list(map(int,input().split()))
    grid.append(p)


# 全探索
ans = 0
for i in range(1,2**h):
    rows = []
    for j in range(h):
        if i >> j&1:
            rows.append(h-j-1)

    memo = {}
    # row_colの値が等しいかチェック
    for col in range(w):
        now = 0
        for row in rows:
            if not now:
                now = grid[row][col]
            else:
                if now != grid[row][col]:
                    break
        else:
            if now in memo:
                memo[now] += len(rows)
            else:
                memo[now] = len(rows)
    if not len(memo): continue

    ans = max(ans,max(memo.values()))

print(ans)
