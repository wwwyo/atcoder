# 10^5
n = int(input())
a = list(map(int,input().split()))

sum_a = sum(a)
if sum_a % 10 != 0:
    print('No')
    exit()
else:
    ans = sum_a//10
    a+=a
    sum_part = 0
    start = 0
    for i in range(2*n):
        sum_part += a[i]
        if sum_part == ans:
            print('Yes')
            exit()
        elif sum_part > ans:
            while sum_part > ans:
                sum_part -= a[start]
                start += 1
            if sum_part == ans:
                print('Yes')
                exit()
print('No')

