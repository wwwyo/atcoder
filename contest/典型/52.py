# max(n) = 100
n = int(input())
mod = 10**9+7
s = 1

for _ in range(n):
    s *= sum(map(int,input().split()))
print(s % mod)


2,3,4,5,6
1,2,4,4,5

2 * (1+2+3+4+5)
3 * (1+2+4+4+5)
4 * (1+2+3+4+5)

