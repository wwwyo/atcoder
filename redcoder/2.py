
n = int(input())

def divisor(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            cnt+=1
    return cnt

ans = 0
for i in range(1,n+1,2):
    if divisor(i) == 8:
        ans+=1
print(ans)