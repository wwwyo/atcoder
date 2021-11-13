n,k,a = map(int,input().split())

if n == 1:
    print(1)
    exit()
rem = k % n
if (a+rem-1) <= n:
    print(a+rem-1)
else:
    print(a+rem-1-n)