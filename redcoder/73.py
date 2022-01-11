
import math
# 二項係数
def c(n,r):
    r = min(r,n-r)
    # 高速で求める
    # return ( math.factorial(n) // (math.factorial(r) * math.factorial(n-r)) )%mod
    # ! フェルマーの小定理
    # math.factorial(n) %mod * (math.factorial(r)**(mod-2) %mod) * (math.factorial(n-r)**(mod-2) %mod)
    if r == 0:
        return 1
    elif r < 0:
        return 0
    else:
        ans = 1
        x = 1
        y = 1
        for i in range(r):
            x *= (n-i)
            x %= mod
            y *= (i+1)
            y %=mod
        ans *= x %mod * pow(y,mod-2,mod) %mod
        return ans


# 10**6
x_g,y_g = map(int,input().split())
mod = 10**9+7
# a回,b回出たとする
d = [(1,2),(2,1)]
if (2*x_g - y_g) % 3 != 0 or (2*y_g - x_g) %3 != 0:
    print(0)
    exit()

a = (2 * x_g - y_g) //3
b = (2*y_g - x_g) //3

print(c(a+b,a))


