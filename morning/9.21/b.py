a,b = map(int,input().split())

for x in range(1,100000):
    if int(x * 0.08) == a and int(x * 0.1) == b:
        print(x)
        break
else:
    print(-1)
