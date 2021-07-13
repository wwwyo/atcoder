n,y = map(int,input().split())
if 10000*n == y:
    print(n,0,0)
    exit()
for i in range(n+1):
    for j in range(n-i+1):
        if 10000*i+5000*j+1000*(n-i-j) == y:
            print(i,j,n-i-j)
            exit()
print(-1,-1,-1)