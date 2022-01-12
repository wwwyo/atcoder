
import math
mod = 10**9+7
# 10**5

n = int(input())
k = int(input())

def nCr(n,r):
    r = min(r,n-r)
    ans = 1
    inv = 1
    for i in range(r):
        ans *= (n-i)
        ans %= mod
        inv *= (i+1)
        inv %= mod
    return ans * pow(inv, mod-2,mod) % mod


    # return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

print(nCr(n+k-1,k))


# 逆元
# フェルマーの小定理
# n**(p-1) ≡ 1 mod p
# n**(p-2) ≡ n**(-1) mod p 


