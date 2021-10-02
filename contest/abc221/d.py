n = int(input())
cnt = []
ans = [0] * (n+1)
# ログインとログアウトの日付を別で管理する
# ダメな例＝＞でやってたlist[(ログイン日,ログアウト日)]
# ＊累積 accumulate

for _ in range(n):
    a,b = map(int,input().split())
    start = a
    end = a+b
    cnt.append((start,+1))
    cnt.append((end,-1))

cnt.sort()

user = 0
last = -1
# a ~ lastの間の日にちはユーザー数同じ
for a,b in cnt:
    ans[user] += a - last
    last = a
    user += b
    # 最後は0人になるから今回は関係ない

print(*ans[1:])