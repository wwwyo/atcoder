import math

n,m = map(int,input().split())
a_list = list(map(int,input().split()))

ans = [1] * m

# 素因数分解
def primeFactorization(n, primes):
    s = int(math.sqrt(n))+1
    for i in range(2, s):
        if n % i == 0:
            cnt = 0
            while True:
                cnt += 1
                n //= i
                if n % i != 0:
                    primes.add(i)
                    break
    if n != 1:
        primes.add(n)
    return primes

primes = set()
for a in a_list:
    primes = primeFactorization(a, primes)

for prime in sorted(primes):
    if prime > m: break
    if ans[prime-1] == 0: continue
    for i in range(prime, m + 1, prime):
        ans[i-1] = 0

print(ans.count(1))
for idx,a in enumerate(ans):
    if a == 1:
        print(idx+1)

