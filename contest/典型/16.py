# n = 10 ** 9
n = int(input())
a,b,c = map(int,input().split())

ans = 10**4
for i in range(10**4):
    if (a * i) > n: break
    for j in range(10**4-i):
        remain = n - (a * i) - (b * j)
        if remain < 0: break
        if remain % c != 0: continue

        sum_ = i + j + remain // c
        if sum_ < 10 ** 4:
            ans = min(ans, sum_)

print(ans)