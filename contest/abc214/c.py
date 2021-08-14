n = int(input()) # 2*10**5
s = list(map(int,input().split()))
ans = list(map(int,input().split()))

min_idx = ans.index(min(ans))
for i in range(min_idx+1, min_idx+n):
    if i >= n:
        i = (i - n)
    ans[i] = min(ans[i], ans[i-1]+s[i-1])

for m in ans:
    print(m)