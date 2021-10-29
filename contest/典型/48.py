# max(n) = 2 * 10^5
# max(k) = 4 * 10^5
n,k = map(int,input().split())

ab = []
# 1分でb点
# 2分でa点

for _ in range(n):
    a,b = map(int,input().split())
    da = a - b
    ab.append(da)
    ab.append(b)

ab.sort(reverse=True)
print(sum(ab[:k]))


