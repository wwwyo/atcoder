import collections
_ = int(input())
a = list(collections.Counter(map(int,input().split())).items())
n = len(a)
ans = 0

for i in range(n-1):
  for j in range(i+1,n):
    ans+=(a[i][0]-a[j][0])**2*a[i][1]*a[j][1]
print(ans)