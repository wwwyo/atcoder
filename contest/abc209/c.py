n = int(input())
c = list(map(int,input().split()))
c.sort()
ans = 1
for i in range(n):
  ans=(ans*(c[i]-i))%(10**9+7)
print(int(ans%(10**9+7)))

