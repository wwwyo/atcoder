n = int(input())
# info = [map(int,input().split()) for _ in range(n-1)]

cnt=0
for i in range(n):
    for j in range(i+1,n+1):
        cnt+=1
print(cnt)