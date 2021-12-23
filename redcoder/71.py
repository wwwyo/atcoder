
mod = 1000000007
# 10^5
n,q = map(int,input().split())
# (a_i-1) ** a_i
a = list(map(int,input().split()))
c = [0] + list(map(lambda x: int(x)-1,input().split())) + [0]
distance_memo = [0] * n
# iにたどり着くまでにかかる累積和
for i in range(1,n):
    distance_memo[i] = (pow(a[i-1],a[i],mod) + distance_memo[i-1]) % mod

distance = 0
for i in range(q+1):
    if c[i] < c[i+1]:
        distance += (distance_memo[c[i+1]]-distance_memo[c[i]])
    else:
        distance += (distance_memo[c[i]]-distance_memo[c[i+1]])
    distance %= mod


print(distance)