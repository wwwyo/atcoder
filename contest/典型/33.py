# max100
h, w = map(int, input().split())

if h == 1 or w == 1:
    print(h*w)
    exit()
print((h+1)//2 * ((w+1)//2))
