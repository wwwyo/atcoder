n, k = map(int, input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ans = k

for l in ab:
    if l[0] <= ans:
        ans += l[1]
    else:
        break
if ans >= 10**100:
    print(10**100)
else:
    print(ans)
