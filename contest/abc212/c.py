import numpy as np

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 10**7

for i in range(len(a)):
    ans = min(ans,np.amin(np.abs(np.array(b) - a[i])))

print(ans)
