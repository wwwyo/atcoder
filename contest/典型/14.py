# 学校と家を結んだ線が交差していないと最適解
# 10^5
n = int(input())
# a,b = 10^9
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
ans = 0
for i, j in zip(a, b):
    ans += abs(i-j)
print(ans)
