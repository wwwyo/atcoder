# max(n,q) = 10 ^5
n,q = map(int,input().split())
a = list(map(int,input().split()))
shift = 0

for _ in range(q):
    t,x,y = map(int,input().split())
    if t == 1:
        x = (x - shift) % (n) -1
        y = (y - shift) % (n) -1
        a[x],a[y] = a[y],a[x]
    elif t == 2:
        shift+=1
    elif t == 3:
        x = (x-shift) % n -1
        print(a[x])

