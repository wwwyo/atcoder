n = int(input())
a = list(map(int,input().split()))
x = int(input())

sum_a = sum(a)
loop = x // sum_a
remain = x % sum_a

loop * n
sum_b = 0
for i in range(n):
    sum_b += a[i]
    if sum_b > remain:
        print(loop*n + i+1)
        break
