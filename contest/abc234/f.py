
import collections
import math
mod = 998244353
# 5000
s = input()
s_int = int(s)
s_lst = list(s)

def c(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r)) %mod


ans = 1
for i,cnt in zip(range(len(s_lst)), collections.Counter(s_lst)):
    ans *= c(s_int,i) * math.factorial(i) %mod 
for key, val in :
    ans //= math.factorial(val)
print(ans)
