S = list(input())
acgt = ['A','C','G','T']
cnt = 0
ans = 0
for s in S:
    if s in acgt:
        cnt += 1
        ans = max(cnt,ans)
    else:
        cnt = 0

print(ans)
