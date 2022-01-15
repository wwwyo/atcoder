
# 10**5
n = int(input())
h = list(map(int,input().split()))

now = 0
for i in range(n):
    next = h[i]
    if next > now:
        now = next
    else:
        break

print(now)
