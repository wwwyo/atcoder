# max(n,q) = 10^5
n,q = map(int,input().split())
a = list(map(int,input().split()))
diff = [0] * (n-1)
for i in range(n-1):
    diff[i] = a[i+1]-a[i]
all_diff = sum(map(abs, diff))

for _ in range(q):
    # 上げ下げをメモ
    l,r,v = map(int,input().split())
    l-=1
    r-=1
    if l > 0:
        all_diff -= abs(diff[l-1])
        diff[l-1] += v
        all_diff += abs(diff[l-1])
    if r < (n-1):
        all_diff -=abs(diff[r])
        diff[r] -= v
        all_diff += abs(diff[r])
    print(all_diff)

