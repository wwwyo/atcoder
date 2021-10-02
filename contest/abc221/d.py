n = int(input())

memo = [0] * n
# i日目の変化量をメモしていく
ab = [list(map(int ,input().split())) for _ in range(n)]
ab.sort()
for i in range(n):
    lst = ab[i]
    memo[lst[0]] += 1
    memo[lst[1]] -= 1
lst.sort()

