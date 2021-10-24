# a * b = 最大公約数 + 最小公倍数
import math
# a > b
def gcd(a,b):
    if a == b: return a

    remain = a % b
    if remain == 0:
        return b
    return gcd(b,remain)

a,b = map(int,input().split())
a,b  = max(a,b),min(a,b)

l = a // gcd(a,b) * b
if l > 10**18:
    print('Large')
else:
    print(l)


