# n = 10**5
n = int(input())
a = list(map(int,input().split()))

xor = a[0]^a[1]
for i in range(n):
    xor ^=a[i]
    if xor != 0:
        continue
    if (n-i) %2 == 0:
        print("")

if xor in a:
    print('Win')
else:
    print('Lose')