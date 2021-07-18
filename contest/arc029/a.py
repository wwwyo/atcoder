n = int(input())
t = [int(input()) for _ in range(n)]
ans = 50*2

for i in range(2**n):
    a = []
    b = []
    for j in range(n):
        if i >> j &1:
            a.append(t[j])
        else:
            b.append(t[j])
    ans = min(ans,max(sum(a), sum(b)))

print(ans)