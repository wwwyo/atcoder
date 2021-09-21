n, q = map(int,input().split())

a = list(map(int,input().split()))

for i in range(q):
    t,x,y = map(int,input().split())

    if t == 1:
        a[x-1] = a[x-1] ^ y
    else:
        print(eval('^'.join(map(str, a[x-1:y]))))
