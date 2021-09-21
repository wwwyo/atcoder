a,b = map(int,input().split())

c = (2 * a + 100) - b
if c >= 0:
    print(c)
else:
    print(0)