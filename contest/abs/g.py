n = int(input())
a = list(map(int,input().split()))

if n == 1:
    print(a[0])
    exit()
a.sort(reverse=True)
print(sum(a[::2])-sum(a[1::2]))
