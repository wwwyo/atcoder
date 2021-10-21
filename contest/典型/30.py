import math
# n = 10 ^ 7
# 1 <= k <= 8
n, k = map(int, input().split())


def primeFactorize(n):
    if n == 1:
        return [1]

    prime_factorizes = []
    while n % 2 == 0:
        prime_factorizes.append(2)
        n //= 2

    divide = 3
    while divide < n:
        if n % divide == 0:
            prime_factorizes.append(divide)
            n //= divide
        else:
            divide += 2
    if n != 1:
        prime_factorizes.append(n)
    return prime_factorizes


# 素因数の種類がk以上の時、素因数から構成される数を削除する。
ans = 0
iter = dict(enumerate(range(1, n+1)))
for i in range(n+1):
    v = iter[i]
    if v == 0:
        continue
    factors = primeFactorize(v)
    if len(set(factors)) >= k:
        ans += 1
        for j in range(2, n):
            j *= v
            if j > n:
                break
            if not iter[j]:
                continue
            ans += 1
            iter[j] = 0
print(ans)
