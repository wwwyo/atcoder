
mod = 1000000007
m,n = map(int,input().split())

# xのn乗
# 指数部を減らせば計算量がlog(n)まで落ちる
def pow(x,n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow(x**2, n//2) %mod
    else:
        return x * pow(x**2,(n-1)//2)%mod
    
# より早く
def pow_k(x,n):
    if n==0:
        return 1
    # 係数
    k = 1
    while n > 1:
        if n % 2 == 0:
            x = x**2 %mod
            n //=2
        else:
            k = k*x %mod
            x = x**2 %mod
            n = (n-1)//2
    return k * x %mod

        



# nを２の指数乗で表す
# m**(2**x)
print(pow_k(m,n))
