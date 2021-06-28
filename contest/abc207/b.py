a,b,c,d = map(int,input().split())
blue = a
red = 0
cnt = 0
if a + b*10**10 > c * 10**10 * d:
    print(-1)
    exit()
while True:
    if blue<=red*d:
        print(cnt)
        break
    blue+=b
    red+=c
    cnt+=1